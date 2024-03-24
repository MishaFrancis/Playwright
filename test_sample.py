from playwright.sync_api import sync_playwright

with sync_playwright() as m:

    browser = m.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com/")
    page.get_by_role("button", name="Alles afwijzen").click()
    page.get_by_label("Zoek", exact=True).click()
    page.get_by_label("Zoek", exact=True).fill("Hoofddorp")
    page.get_by_role("button", name="Google Zoeken").click()
    page.wait_for_timeout(10000)
