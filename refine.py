import os
import google.generativeai as genai
from dotenv import load_dotenv
import asyncio
import sys

# --- ⚠️ CONFIGURATION ---
FAILED_COMPONENT_NAME = "Sidebar"
TEST_ERROR_MESSAGE = 'AssertionError: expect(locator).to_have_css("background-color", "rgb(37, 40, 47)")'
EXPECTED_VALUE = "rgb(37, 40, 47)"

COMPONENT_PATH = f"output/cloned_app/app/components/{FAILED_COMPONENT_NAME}.tsx"


async def run_refinement():
    """
    This script demonstrates the "self-correction" capability of the agent.
    """
    print(f"--- 🚀 STARTING AGENT REFINEMENT for <{FAILED_COMPONENT_NAME} /> ---")

    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("❌ Error: GOOGLE_API_KEY not found in .env file.")
        sys.exit(1)
    genai.configure(api_key=api_key)

    print(f"   -> Loading broken code from {COMPONENT_PATH}...")
    try:
        with open(COMPONENT_PATH, "r", encoding="utf-8") as f:
            broken_code = f.read()
    except FileNotFoundError:
        print(f"❌ Error: Broken component file not found at {COMPONENT_PATH}")
        sys.exit(1)

    print("   -> Building refinement prompt...")
    system_prompt = f"""
    You are an expert, world-class frontend engineer. Your job is to fix bugs.
    A component you generated has failed a CSS test.
    You must generate the new, corrected version of the code.

    RULES:
    1.  **PIXEL-PERFECT accuracy is mandatory.**
    2.  You MUST fix the specific error.
    3.  Output *only* the complete, raw, corrected `.tsx` code.
    4.  **DO NOT** include any other text, explanations, or markdown fences (```).
    """

    user_prompt = f"""
    Here is the component that failed: `{FAILED_COMPONENT_NAME}.tsx`

    Here is the test error it produced:
    `{TEST_ERROR_MESSAGE}`

    This error means the component was *expected* to have a CSS property of `{EXPECTED_VALUE}`, but it did not.
    You must update the code to have this exact style.

    Here is the original, INCORRECT code:
    ```tsx
    {broken_code}
    ```

    Please generate the new, corrected `.tsx` code now.
    """

    print("   -> Calling Gemini (gemini-2.5-flash) for a fix...")
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = await model.generate_content_async(
            [system_prompt, user_prompt],
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=8192,
            )
        )

        corrected_code = response.text

        if corrected_code.startswith("```tsx"):
            corrected_code = corrected_code.split("```tsx\n", 1)[1]
            corrected_code = corrected_code.rsplit("```", 1)[0]
        elif corrected_code.startswith("```"):
            corrected_code = corrected_code.split("\n", 1)[1]
            corrected_code = corrected_code.rsplit("```", 1)[0]

        print("\n--- ✅ AI SUGGESTED FIX ---")
        print(corrected_code)
        print("----------------------------")
        print(f"\nTo apply this fix, copy the code above and paste it into {COMPONENT_PATH}")

    except Exception as e:
        print(f"❌ Error during Google AI API call: {e}")


if __name__ == "__main__":
    asyncio.run(run_refinement())