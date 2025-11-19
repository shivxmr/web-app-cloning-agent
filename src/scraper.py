import asyncio
from playwright.async_api import async_playwright, Page
from bs4 import BeautifulSoup
import os

AUTH_FILE = "data/session.json"
SCREENSHOT_PATH = "data/screenshots/asana_page.png"
DOM_PATH = "data/dom/asana_page.html"


async def capture_page_state(url: str):
    """
    Loads an authenticated session, navigates to a URL,
    and scrapes its screenshot and DOM.
    """
    if not os.path.exists(AUTH_FILE):
        print(f"❌ [ERROR] Authentication file missing at: {AUTH_FILE}")
        print("   -> Action Required: Run 'python auth.py' to generate this file.")
        return None, None

    print(f"🚀 [Scraper] Initializing Playwright browser session...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # Run headless now

        context = await browser.new_context(storage_state=AUTH_FILE)
        page = await context.new_page()

        print(f"🌐 [Scraper] Navigating to target URL: {url}")
        try:
            await page.goto(url, wait_until="networkidle", timeout=30000)
        except Exception as e:
            print(f"⚠️ [WARNING] Navigation timeout or error: {e}")
            print("   -> Proceeding with current page state...")

        await page.wait_for_timeout(8000)

        print(f"📸 [Scraper] Capturing full-page screenshot...")
        await page.screenshot(path=SCREENSHOT_PATH, full_page=True)

        print(f"📄 [Scraper] Extracting and minifying DOM structure...")
        html_content = await page.content()

        soup = BeautifulSoup(html_content, 'html.parser')

        for s in soup(['script', 'style', 'link']):
            s.decompose()

        body = soup.find('body')
        if body:
            clean_html = str(body)
        else:
            clean_html = str(soup)

        with open(DOM_PATH, "w", encoding="utf-8") as f:
            f.write(clean_html)

        await browser.close()

        print("✅ [Scraper] Page state captured successfully.")
        print(f"   -> Screenshot: {SCREENSHOT_PATH}")
        print(f"   -> DOM File:   {DOM_PATH}")

        return SCREENSHOT_PATH, DOM_PATH


if __name__ == "__main__":
    # --- IMPORTANT ---
    # 1. Log in to Asana (using setup_auth.py)
    # 2. Go to the "Projects" page or a specific Kanban board.
    # 3. Copy that URL and paste it here.

    # Example URL (replace this with your own):
    TARGET_URL = "https://app.asana.com/1/1211954934787771/home"

    if TARGET_URL == "hi":
        print("=" * 50)
        print("=" * 50)
        print(f"❌ [ERROR] Invalid Target URL in {os.path.basename(__file__)}")
        print("   -> Please update the 'TARGET_URL' variable.")
        print("=" * 50)
        print("=" * 50)
    else:
        asyncio.run(scrape_page(TARGET_URL))