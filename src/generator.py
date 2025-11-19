import os
import google.generativeai as genai
from dotenv import load_dotenv
import PIL.Image
import json
import asyncio

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise EnvironmentError("GOOGLE_API_KEY is missing. Ensure it exists in your .env configuration file.")
genai.configure(api_key=api_key)

SCREENSHOT_PATH = "data/screenshots/asana_page.png"
DOM_PATH = "data/dom/asana_page.html"


# --- UTILITY FUNCTIONS ---

def read_dom_file():
    """Retrieves the sanitized DOM content."""
    with open(DOM_PATH, "r", encoding="utf-8") as f:
        return f.read()


def load_image():
    """Imports the captured screenshot."""
    return PIL.Image.open(SCREENSHOT_PATH)


async def call_gemini_async(model_name: str, prompt_parts: list, is_json: bool = False):
    """Utility function for invoking the Gemini API with automatic retry logic."""
    print(f"   -> [Gemini API] Dispatching API request to '{model_name}' endpoint...")

    max_retries = 2
    for attempt in range(max_retries): 
        try:
            model = genai.GenerativeModel(model_name)

            generation_config = genai.types.GenerationConfig(
                candidate_count=1,
                max_output_tokens=32768,
                temperature=0.1
            )

            if is_json:
                generation_config.response_mime_type = "application/json"

            response = await model.generate_content_async(
                prompt_parts,
                generation_config=generation_config
            )
            return response.text

        except Exception as e:
            print(f"❌ [ERROR] API communication error (Attempt {attempt + 1}/{max_retries}).")
            print(f"   -> Error details: {e}")
            if "504" in str(e):
                print("   -> 504 Gateway Timeout detected. Backend service overloaded or request too demanding.")
                if attempt < max_retries - 1:
                    print("   -> [Retry Logic] Pausing 10 seconds before reattempting due to timeout...")
                    await asyncio.sleep(10)
            elif attempt < max_retries - 1:
                print("   -> Reattempting in 5 seconds...")
                await asyncio.sleep(5)

            if attempt == max_retries - 1:
                print("❌ [CRITICAL] Retry limit exhausted. Content generation unsuccessful for this component.")
                return None
    return None


# --- CORE AGENT OPERATIONS ---

async def analyze_layout(dom_content: str, img: PIL.Image.Image):
    """
    Phase 1: Utilizes the 'flash' model to extract a CONCISE COMPONENT LIST.
    """
    print("🧠 [Generator] Phase 1: Dissecting page architecture to detect component hierarchy...")

    prompt_parts = [
        "You are an experienced UI architect. Examine this webpage screenshot alongside its DOM structure to determine its **primary, top-level architectural components**.",
        "Objective: Provide the **minimal collection of the most prominent components** constituting the interface. Avoid granular sub-elements (e.g., consolidate 'Logo', 'Searchbar', and 'ProfileIcon' into simply 'Header').",
        "Deliver your analysis as a JSON object containing one key 'components', whose value is a string array.",
        "**MANDATORY CONSTRAINTS:**",
        "1. All entries must be **unique** - no duplicates permitted.",
        "2. Component identifiers MUST follow `PascalCase` convention as single words (e.g., 'ProjectHeader', 'TaskList'). **Spaces and hyphens are forbidden.**",
        "Sample output: { \"components\": [\"Sidebar\", \"Header\", \"ProjectKanbanBoard\"] }",
        "\n--- DOM Structure ---",
        dom_content,
        "\n--- Visual Reference ---",
        img,
        "Provide exclusively the JSON object."
    ]

    response_text = await call_gemini_async(
        'gemini-2.5-flash',
        prompt_parts,
        is_json=True
    )

    if not response_text:
        return None

    try:
        data = json.loads(response_text)
        components = data.get("components")
        if not components or not isinstance(components, list):
            print(f"❌ [Generator] Malformed API response. Component list expected but not received.")
            print(f"   -> Unprocessed output: {response_text}")
            return None

        print(f"✅ [Generator] Structural analysis completed successfully: {components}")
        return components
    except json.JSONDecodeError:
        print(f"❌ [Generator] JSON parsing error encountered.")
        print(f"   -> Unprocessed output: {response_text}")
        return None


async def generate_component(component_name: str, dom_content: str, img: PIL.Image.Image):
    """
    Phase 2a: Engages the 'pro' model for premium code generation.
    """
    print(f"🧠 [Generator] Phase 2a (Pro): Producing production-grade implementation for <{component_name} />...")

    system_prompt = f"""
    You are a seasoned, elite-level frontend developer. Your objective is to create code for an individual React component: `{component_name}`.

    **PRECISION IS PARAMOUNT.**

    REQUIREMENTS:
    1.  **VISUAL FIDELITY:** Your output *must* replicate the screenshot exactly.
        * **Color Palette:** Achieve pixel-perfect color accuracy. Utilize Tailwind utility classes or precise hex values.
        * **Typography:** Replicate font styles, weights, and dimensions.
        * **Layout Spacing:** Preserve all margin and padding measurements.
    2.  **'use client';:** When utilizing *any* React Hooks (such as `useState`), the directive `'use client';` MUST appear as the *initial line*.
    3.  **PACKAGE DECLARATIONS:** Following 'use client;' (when applicable), include a single-line JSON comment enumerating external NPM packages.
        Format: `// {{"dependencies": ["lucide-react"]}}`
        When absent, specify: `// {{"dependencies": []}}`
    4.  **SAFE CODING:** When referencing variables in JSX (e.g., `projectName.length`), ALWAYS provide fallback values to avoid `undefined` exceptions.
    5.  **MODULE IMPORTS:** Include ALL required import statements.
    6.  **RAW OUTPUT:** Deliver *exclusively* the `.tsx` source code. **NEVER include ```tsx or ``` markers. NEVER append explanatory text.**
    7.  **MODULE EXPORT:** Use default export syntax (e.g., `export default function {component_name}() {{...}}`).
    """

    prompt_parts = [
        system_prompt,
        "\n--- DOM Structure (reference material) ---",
        dom_content,
        "\n--- Visual Design (reference material) ---",
        img,
        f"Proceed to generate the `{component_name}` component implementation, adhering strictly to all specified requirements."
    ]

    return await call_gemini_async('gemini-2.5-pro', prompt_parts)


async def generate_component_code_flash(component_name: str, dom_content: str, img: PIL.Image.Image):
    """
    Phase 2b: Utilizes the 'flash' model for rapid fallback code synthesis.
    """
    print(f"🧠 [Generator] Phase 2b (Flash): Creating backup implementation for <{component_name} />...")

    system_prompt = f"""
    You are an efficient frontend developer. Generate code for a standalone React component: `{component_name}`.

    **PRECISION REMAINS THE TOP PRIORITY.**

    REQUIREMENTS:
    1.  **VISUAL FIDELITY:** Your output *must* replicate the screenshot exactly.
        * **Color Palette:** Achieve pixel-perfect color accuracy. Utilize Tailwind utility classes or precise hex values.
        * **Typography:** Replicate font styles, weights, and dimensions.
        * **Layout Spacing:** Preserve all margin and padding measurements.
    2.  **'use client';:** When utilizing *any* React Hooks (such as `useState`), the directive `'use client';` MUST appear as the *initial line*.
    3.  **PACKAGE DECLARATIONS:** Following 'use client;' (when applicable), include a single-line JSON comment enumerating external NPM packages.
        Format: `// {{"dependencies": ["lucide-react"]}}`
        When absent, specify: `// {{"dependencies": []}}`
    4.  **SAFE CODING:** When referencing variables in JSX (e.g., `projectName.length`), ALWAYS provide fallback values to avoid `undefined` exceptions.
    5.  **MODULE IMPORTS:** Include ALL required import statements.
    6.  **RAW OUTPUT:** Deliver *exclusively* the `.tsx` source code. **NEVER include ```tsx or ``` markers. NEVER append explanatory text.**
    7.  **MODULE EXPORT:** Use default export syntax (e.g., `export default function {component_name}() {{...}}`).
    """

    prompt_parts = [
        system_prompt,
        "\n--- DOM Structure (reference material) ---",
        dom_content,
        "\n--- Visual Design (reference material) ---",
        img,
        f"Proceed to generate the `{component_name}` component implementation, adhering strictly to all specified requirements."
    ]

    return await call_gemini_async('gemini-2.5-flash', prompt_parts)


def parse_code_response(raw_response: str, component_name: str):
    """
    Extracts executable code and package requirements from the LLM output.
    """
    if not raw_response:
        return None, []

    dependencies = []
    generated_code = ""
    use_client = False

    try:
        lines = raw_response.split('\n')

        json_line_index = -1

        for i, line in enumerate(lines):
            stripped_line = line.strip()
            if stripped_line.startswith("//") and "dependencies" in stripped_line:
                try:
                    json_str = stripped_line.lstrip("//")
                    dep_data = json.loads(json_str)
                    dependencies = dep_data.get("dependencies", [])
                    json_line_index = i
                except json.JSONDecodeError:
                    pass
            elif stripped_line == "'use client';" or stripped_line == '"use client";':
                use_client = True

        code_lines = []
        for i, line in enumerate(lines):
            stripped_line = line.strip()
            if i == json_line_index: continue
            if stripped_line == "```" or stripped_line == "```tsx": continue
            code_lines.append(line)

        generated_code = "\n".join(code_lines).strip()

        if not use_client and (
                "useState" in generated_code or "useEffect" in generated_code or "useRef" in generated_code):
            print(f"⚠️ [Generator] Auto-Fix Applied: Injected missing 'use client' declaration to <{component_name} />.")
            generated_code = f"'use client';\n\n{generated_code}"

        print(f"✅ [Generator] Response processing completed for <{component_name} />.")
        print(f"   -> Identified packages: {dependencies}")
        return generated_code, dependencies

    except Exception as e:
        print(f"❌ [Generator] Response parsing exception for <{component_name} />: {e}")
        return generated_code, []