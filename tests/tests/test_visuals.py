import pytest
from playwright.sync_api import Page, expect
import os
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch

# --- Configuration ---
ORIGINAL_ASANA_SCREENSHOT = "storage/screenshots/asana_page.png"
CLONE_SCREENSHOT_PATH = "storage/screenshots/clone_page_test.png"
DIFF_PATH = "storage/screenshots/clone_diff.png"
APP_URL = "http://localhost:3000"


def test_visual_regression(page: Page):
    """
    Takes a screenshot of the clone and compares it to the original
    using the 'pixelmatch' library. This also quantifies the
    visual accuracy percentage.
    """
    print(f"\nNavigating to {APP_URL} for visual test...")
    page.goto(APP_URL, wait_until="networkidle")

    page.wait_for_selector("main")

    print("Taking screenshot of clone...")

    # Mask dynamic content
    dynamic_locators = [
        page.get_by_role("heading", name="Bikash Agarwal"),
        page.locator("time"),
        page.get_by_text("Today"),
    ]

    page.screenshot(
        path=CLONE_SCREENSHOT_PATH,
        full_page=True,
        mask=dynamic_locators
    )

    print("Loading screenshots for comparison...")

    if not os.path.exists(ORIGINAL_ASANA_SCREENSHOT):
        pytest.fail(f"Original screenshot not found at {ORIGINAL_ASANA_SCREENSHOT}")

    img_a = Image.open(ORIGINAL_ASANA_SCREENSHOT).convert("RGBA")
    img_b = Image.open(CLONE_SCREENSHOT_PATH).convert("RGBA")

    # --- QUANTIFICATION STEP ---
    if img_a.size != img_b.size:
        print(f"⚠️ Warning: Image sizes differ. Resizing clone image...")
        img_b = img_b.resize(img_a.size)

    total_pixels = img_a.size[0] * img_a.size[1]
    img_diff = Image.new("RGBA", img_a.size)

    mismatched_pixels = pixelmatch(
        img_a,
        img_b,
        output=img_diff,
        threshold=0.1
    )

    if mismatched_pixels > 0:
        img_diff.save(DIFF_PATH)
        print(f"🚨 Visual diff saved to {DIFF_PATH}")

    # --- QUANTIFICATION REPORT ---
    mismatch_percent = (mismatched_pixels / total_pixels) * 100
    accuracy_percent = 100.0 - mismatch_percent

    print(f"📊 Pixel Mismatch: {mismatched_pixels} pixels ({mismatch_percent:.2f}%)")
    print(f"🔥 Visual Accuracy: {accuracy_percent:.2f}%")

    # --- ASSERTION ---
    assert accuracy_percent > 90, \
        f"Visual Accuracy {accuracy_percent:.2f}% is below 90% threshold. See {DIFF_PATH}"

    print("✅ Visual regression test passed.")


def test_css_assertions(page: Page):
    """
    Checks the computed CSS properties of specific elements.
    """
    print(f"\nNavigating to {APP_URL} for CSS tests...")
    page.goto(APP_URL, wait_until="networkidle")

    # 1. Test 'Create' Button
    create_button = page.get_by_role("button", name="Create")

    if create_button.count() == 0:
        pytest.fail("CSS Test: Could not find 'Create' button.")

    expect(create_button.first).to_have_css("color", "rgb(255, 255, 255)")
    print("✅ CSS Test: 'Create' button text color is correct.")

    print("✅ CSS assertion tests complete.")