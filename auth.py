import asyncio
from playwright.async_api import async_playwright
import os

AUTH_FILE = "data/session.json"


async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://app.asana.com/-/login")

        print("\n" + "=" * 60)
        print("🔒 [AUTH REQUIRED] Please log in to Asana in the opened browser.")
        print("   1. Enter your credentials.")
        print("   2. Wait for the dashboard to load.")
        print("   3. Return to this terminal and PRESS ENTER.")
        print("=" * 60 + "\n")

        # Wait for user to press Enter
        await asyncio.to_thread(input)

        print("✅ [Auth] User confirmation received. Capturing session state...")

        try:
            await context.storage_state(path=AUTH_FILE)
            print(f"✅ [Auth] Session state successfully saved to: '{AUTH_FILE}'")
        except Exception as e:
            print(f"❌ [ERROR] Failed to save session state: {e}")

        await browser.close()
        print("✅ [Auth] Browser session closed.")


if __name__ == "__main__":
    if os.path.exists(AUTH_FILE):
        os.remove(AUTH_FILE)
        print(f"🗑️  [Auth] Removed existing auth file: {AUTH_FILE}")

    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print("\n⚠️ [Auth] Process interrupted by user.")