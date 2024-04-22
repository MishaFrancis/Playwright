import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_milk_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.dirk.nl/")
    page.wait_for_load_state()
    page.get_by_placeholder("Ik zoek...").fill("melk")
    page.get_by_placeholder("Ik zoek...").press("Enter")
    page.get_by_role("img", name="de Beste Volle melk").click()
    expect(page.get_by_role("heading", name="de Beste Volle melk")).to_be_visible()
    page.get_by_role("heading", name="de Beste Volle melk").highlight()
    page.get_by_placeholder("Ik zoek...").fill("melk")
    page.get_by_placeholder("Ik zoek...").press("Enter")
    expect(page.get_by_role("link", name="de Beste Volle melk")).to_be_visible()
    expect(page.locator("article").filter(has_text="193Melkunie Halfvolle melk1,5").get_by_role("link")).to_be_visible()
    expect(page.get_by_role("link", name="Bio+ Biologische halfvolle")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     test_milk_run(playwright)
