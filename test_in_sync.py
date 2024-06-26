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
    expect(page).to_have_url(re.compile(".*intro"))


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

@pytest.mark.skip(reason="Skipping this test since its failing in headless mode. URL not working..")
def test_hema_home_page_countries(page: Page):

    page.goto("https://corporate.hema.com/en")
    # Expect a title
    page.wait_for_timeout(4000)
    print(page.title())

    # Chek home page header links
    expect(page.get_by_text("about HEMA")).to_be_visible()
    expect(page.get_by_text("news & press")).to_be_visible()
    expect(page.get_by_role("link", name="working at HEMA")).to_be_visible()
    expect(page.get_by_role("link", name="contact")).to_be_visible()

    # Navigate to contact page
    page.get_by_role("link", name="contact").click()

    # Chek contact page countries
    expect(page.get_by_text("the Netherlands", exact=True)).to_be_visible()
    expect(page.get_by_text("Belgium")).to_be_visible()
    expect(page.get_by_text("France")).to_be_visible()
    expect(page.get_by_text("Austria")).to_be_visible()
    expect(page.get_by_text("Germany", exact=True)).to_be_visible()
    expect(page.get_by_text("Luxembourg")).to_be_visible()

    # This is a soft assert in Python. If it fails, stil the remaining part of the test will continue and complete.
    with check:
        assert page.title() == "contact"

    # Expand "about HEMA" header link
    page.get_by_text("about HEMA").click()

    # Check the links under "about HEMA" header link
    expect(page.get_by_role("link", name="about us")).to_be_visible()
    expect(page.get_by_role("link", name="history")).to_be_visible()
    expect(page.get_by_role("link", name="environment")).to_be_visible()
    expect(page.get_by_role("link", name="people and society")).to_be_visible()
    expect(page.get_by_role("link", name="for suppliers")).to_be_visible()
    
    print("Test point")

    page.wait_for_timeout(2000)

    page.close()
 

    
def test_run_cassini_home_page(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=200)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.cassini-technologies.com/")
    expect(page.get_by_role("heading", name="Redefining ophthalmic")).to_be_visible
    expect(page.get_by_text("Discover the future of vision")).to_be_visible
    expect(page.get_by_role("link", name="Request a Demo")).to_be_visible
    page.wait_for_timeout(1000)

    # ---------------------
    context.close()
    browser.close()


@pytest.mark.smoke
def test_shopping_order_confirmation_for_Next_Day_Air(page: Page):

    # Open page
    page.goto("https://demowebshop.tricentis.com/")

    # Expect the page title
    print(page.title())
    expect(page).to_have_title("Demo Web Shop")
    
    ## Login section
    page.get_by_role("link", name="Log in").click()
    page.get_by_label("Email:").fill("mishafrancis@gmail.com")
    page.get_by_label("Password:").fill("Test1234$")
    page.get_by_role("button", name="Log in").click()

    ## Select products from list to shopping cart

    # Item 1
    page.get_by_role("link", name="Apparel & Shoes").first.click()
    page.get_by_role("button", name="Add to cart").nth(2).click()
    # Item 2
    page.get_by_role("link", name="Books").first.click()
    page.get_by_role("button", name="Add to cart").nth(1).click()

    ## Shopping cart
    page.locator("xpath=/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[3]/a").click()
    expect(page.get_by_role("heading", name="Shopping cart")).to_be_visible

    ## Navigate to checkout
    page.wait_for_timeout(500)
    page.locator("#termsofservice").check()
    page.get_by_role("button", name="Checkout").click()
    page.get_by_role("button", name="Continue").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Continue").click()
    page.wait_for_timeout(500)
    # Select shipping type - 'Next Day Air'
    page.get_by_label("Next Day Air (40.00)").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Continue").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Continue").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Continue").click()
    page.wait_for_timeout(500)

    ## validate confirmation page
    expect(page.get_by_role("cell", name="Sub-Total:")).to_be_visible
    expect(page.get_by_role("cell", name="11.00")).to_be_visible
    expect(page.get_by_role("cell", name="Shipping: (Next Day Air)")).to_be_visible
    expect(page.get_by_role("cell", name="40.00")).to_be_visible
    expect(page.get_by_role("cell", name="Payment method additional fee:")).to_be_visible
    expect(page.get_by_role("cell", name="7.00")).to_be_visible
    expect(page.get_by_role("cell", name="Tax:")).to_be_visible
    expect(page.get_by_role("cell", name="0.00", exact=True)).to_be_visible
    expect(page.get_by_role("cell", name="Total:", exact=True)).to_be_visible
    expect(page.get_by_role("cell", name="58.00")).to_be_visible

    ## Validate Order message
    page.get_by_role("button", name="Confirm").click()
    expect(page.get_by_role("heading", name="Thank you")).to_be_visible
    expect(page.get_by_text("Your order has been")).to_be_visible
    expect(page.get_by_text("Order number:")).to_be_visible

    ## Logout & close
    page.get_by_role("link", name="Log out").click()
    page.screenshot(path = "order.jpg", full_page=False)
    page.close()


