import re
import pytest
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from pytest_check import check

def test_has_title(page: Page):
    
    page.goto("https://playwright.dev/")

    # Expect a title
    expect(page).to_have_title(re.compile("Playwright"))

    print('This is a check-point for me. Thanks !')

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_text("Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


def test_get_started_print():
    print("Get started")

def test_fedex_home_page_links(page: Page):
    page.goto("https://www.fedex.com/en-nl/home.html")

    
    # Expect below url
    expect(page).to_have_url('https://www.fedex.com/en-nl/home.html')
    print("URL:"+page.url)

    # For cookie pop-up
    reject_button = page.get_by_role("button", name="REJECT ALL COOKIES")
    if (reject_button.is_visible()):
        reject_button.click()
        print("In headed mode")
        # Expect below links on home page
        expect(page).to_have_title("FedEx | Express Delivery, Courier & Shipping Services | Netherlands")
        expect(page.get_by_label("FedEx Netherlands Homepage")).to_be_visible()
        expect(page.get_by_role("link", name="Shipping", exact=True)).to_be_visible()
        expect(page.get_by_role("link", name="Tracking", exact=True)).to_be_visible()
        expect(page.get_by_role("link", name="Support", exact=True)).to_be_visible()
        expect(page.get_by_role("link", name="Account", exact=True)).to_be_visible()
        expect(page.get_by_role("link", name="Sign in to Fedex.com", exact=True)).to_be_visible()
        print("All header navigation links are visible on "+ page.url)

        # Tracking section
        expect(page.get_by_label("", exact=True)).to_be_visible()
        expect(page.get_by_role("button", name="Click your to track your")).to_be_visible()
        expect(page.get_by_label("Multiple Tracking Numbers")).to_be_visible()
        expect(page.get_by_label("Need Help?")).to_be_visible()

    else:
        print("In headless mode");
        expect(page).to_have_title("FedEx | System Down")
        expect(page.get_by_role("link", name="Shipping", exact=True)).to_be_hidden()


    print("***End***")
    
    page.wait_for_timeout(2000)
    page.close()


@pytest.mark.smoke
def test_hema_home_page_countries(page: Page):

    page.goto("https://corporate.hema.com/en")
    # Expect a title
    page.wait_for_timeout(2000)
    print(page.title())

    page.get_by_role("link", name="contact").click()

    expect(page.get_by_text("the Netherlands", exact=True)).to_be_visible()
    expect(page.get_by_text("Belgium")).to_be_visible()
    expect(page.get_by_text("France")).to_be_visible()
    expect(page.get_by_text("Austria")).to_be_visible()
    expect(page.get_by_text("Germany", exact=True)).to_be_visible()
    expect(page.get_by_text("Luxembourg")).to_be_visible()

    # This is a soft assert in Python. If it fails, still the remaining part of the test will continue and complete.
    with check:
        assert page.title() == "contact"
    
    print("Test point")

    page.wait_for_timeout(2000)

    page.close()

    
