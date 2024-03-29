import re 
from playwright.sync_api import Page, expect, Playwright, sync_playwright

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
    # Expect a title
    expect(page).to_have_title(re.compile("FedEx | Express Delivery, Courier & Shipping Services | Netherlands"))
    
    # Expect below url
    expect(page).to_have_url('https://www.fedex.com/en-nl/home.html')
    print("URL:"+page.url)

    # Expect below links
    expect(page.get_by_role("link", name="Shipping", exact=True)).to_be_visible
    expect(page.get_by_role("link", name="Tracking", exact=True)).to_be_visible
    expect(page.get_by_role("link", name="Support", exact=True)).to_be_visible
    expect(page.get_by_role("link", name="Account", exact=True)).to_be_visible
    print("All header navigation links are visible on "+ page.url)
    page.close()
