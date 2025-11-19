import asyncio
import sys
import os
import re
from src.scraper import capture_page_state
from src.generator import (
    analyze_layout,
    generate_component,
    generate_component_code_flash,
    parse_code_response,
    read_dom_file,
    load_image
)
from src.builder import assemble_project

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

SITE_URL = os.getenv("SITE_URL")

if not SITE_URL:
    print("❌ [ERROR] 'SITE_URL' not found in environment variables.")
    print("   -> Please add it to your .env file.")
    sys.exit(1)

# Define the output directory for the actor
OUTPUT_DIR = "builds/cloned_app"


def sanitize_component_name(name: str) -> str:
    """Removes spaces and invalid chars from component name."""
    name = re.sub(r"\s+", "", name)
    name = re.sub(r"[^a-zA-Z0-9_]", "", name)
    return name


async def main():
    if "YOUR_PROJECT_ID" in SITE_URL:
        print("=" * 50)
        print(f"❌ ERROR: Please update the 'TARGET_URL' in {os.path.basename(__file__)}")
        print("=" * 50)
        sys.exit(1)

    print(f"--- 🚀 CLOONEY AGENT INITIALIZING: {os.path.basename(__file__)} ---")
    print(f"   -> Target Site: {SITE_URL}")
    print(f"   -> Output Directory: {OUTPUT_DIR}")

    # --- STEP 1: OBSERVE ---
    print("\n--- STEP 1: OBSERVING ---")
    if not os.path.exists("storage/screenshots/asana_page.png"):
        await capture_page_state(SITE_URL)
    else:
        print("   -> Using existing observation files in /storage.")
    print("✅ [Step 1] Observation phase completed successfully.")

    # --- STEP 2: THINK (Part 1 - Get Structure) ---
    print("\n--- STEP 2: THINKING (Analyzing Structure) ---")
    dom_content = read_dom_file()
    image = load_image()

    component_list = await analyze_layout(dom_content, image)
    if not component_list:
        print("❌ [CRITICAL ERROR] Agent failed during the Thinking phase (Structure Analysis). Terminating process.")
        return

    # --- STEP 3: THINK (Part 2 - Iterative Loop) ---
    print("\n--- STEP 3: THINKING (Generating Components) ---")
    component_code_map = {}
    all_dependencies = set()

    for component_name in component_list:

        raw_response = await generate_component(component_name, dom_content, image)
        if not raw_response:
            print(f"⚠️  [WARNING] Generator (Pro) encountered an issue for <{component_name} />. Attempting fallback to 'Flash' model...")
            await asyncio.sleep(5)
            raw_response = await generate_component_code_flash(component_name, dom_content, image)

        code, dependencies = parse_code_response(raw_response, component_name)

        print(f"   -> [Rate Limit Control] Pausing for 15 seconds to respect Gemini Pro API limits...")
        await asyncio.sleep(15)

        if not code:
            print(f"❌ [ERROR] Failed to generate valid code for <{component_name} /> after multiple attempts. Skipping component.")
            continue

        sanitized_name = sanitize_component_name(component_name)
        component_code_map[sanitized_name] = code
        all_dependencies.update(dependencies)

    if len(component_code_map) != len(component_list):
        print("❌ [CRITICAL ERROR] Incomplete component generation. Aborting build process to prevent invalid state.")
        return

    print(f"✅ [Step 3] Thinking phase completed. Code generated for {len(component_code_map)} components.")
    print(f"   -> Total dependencies found: {list(all_dependencies)}")

    # --- STEP 4: ACT ---
    print("\n--- STEP 4: ACTING ---")
    try:
        assemble_project(
            component_code_map=component_code_map,
            all_dependencies=all_dependencies,
            output_dir=OUTPUT_DIR
        )
    except Exception as e:
        print(f"❌ [CRITICAL ERROR] Agent failed during the Acting phase: {e}")
        import traceback
        traceback.print_exc()
        return
    print("✅ [Step 4] Acting phase completed. Application assembled successfully.")

    print("\n--- 🥳 AGENT RUN SUCCESSFUL ---")
    print(f"   -> Your cloned app is ready in: '{OUTPUT_DIR}'")
    print(f"   -> To run it: ")
    print(f"      1. cd {OUTPUT_DIR}")
    print(f"      2. pnpm install  (if you haven't)")
    print(f"      3. pnpm run dev")
    print("---------------------------------")


if __name__ == "__main__":
    asyncio.run(main())