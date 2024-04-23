import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_milk_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    ## Navigate to Dirk Home page
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
    page.get_by_role("navigation").get_by_text("Meer", exact=True).click()
    page.get_by_role("navigation").get_by_text("Meer", exact=True).click()
    
    ## Navigate to 'Mijn Dirk' login page
    page.get_by_label("Account").click()

    ## Assert 'Mijn Dirk' login page
    expect(page.get_by_text("Mijn Dirk")).to_be_visible()
    expect(page.get_by_text("E-mailadres")).to_be_visible()
    expect(page.get_by_placeholder("Vul hier je e-mailadres in")).to_be_visible()
    expect(page.get_by_text("Wachtwoord", exact=True)).to_be_visible()
    expect(page.get_by_placeholder("Vul hier je wachtwoord in")).to_be_visible()
    expect(page.get_by_role("link", name="Wachtwoord vergeten?")).to_be_visible()
    expect(page.get_by_role("link", name="Nog geen account?")).to_be_visible()
    expect(page.get_by_text("Onthoud mijn gegevens")).to_be_visible()
    page.get_by_text("Onthoud mijn gegevens").click()
    page.get_by_role("button", name="Aanmelden").click()
    expect(page.get_by_text("Het e-mail veld is verplicht")).to_be_visible()
    expect(page.get_by_text("Het wachtwoord veld is")).to_be_visible()
    expect(page.locator(".alert")).to_be_visible()

    ## ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     test_milk_run(playwright)
