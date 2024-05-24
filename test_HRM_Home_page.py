from playwright.sync_api import sync_playwright, expect,Playwright
import re

def test_Orange_HRM_Home_Page(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    ## Open URL
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    ## Enter details on login page
    page.wait_for_selector('//input[@name="username"]').fill('Admin')
    page.wait_for_selector('//input[@name="password"]').type('admin123')
    page.wait_for_selector('//button[@type="submit"]').click()

    ## Home page
    page.get_by_role("heading", name="Dashboard").highlight()
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
    page.get_by_text("Time at Work").highlight()
    page.wait_for_timeout(2000)
    page.get_by_text("My Actions").highlight()
    page.wait_for_timeout(2000)
    page.get_by_text("Quick Launch").highlight()
    page.wait_for_timeout(2000)
    page.get_by_text("Buzz Latest Posts").highlight()
    page.wait_for_timeout(2000)

    ## Logout
    # page.get_by_role("banner").get_by_role("img", name="profile picture").click()
    # page.locator("xpath=/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i").click()  ## XPath way
    page.wait_for_selector('[class="oxd-icon bi-caret-down-fill oxd-userdropdown-icon"]').click()   ## Using class of the dropdown arrow
    page.get_by_role("menuitem", name="Logout").click()
    expect(page.get_by_role("heading", name="Login")).to_be_visible()
    page.get_by_role("heading", name="Login").highlight()
    page.wait_for_timeout(2000)

    ## Close browser
    browser.close()

    

