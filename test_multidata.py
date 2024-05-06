import pytest
from playwright.sync_api import expect,Playwright

# Parameterize the test function
@pytest.mark.parametrize(
    "username, password, casetype",
    [
        ("Admin", "admin123","Positivecase"),
        ("Bob", "Test1234$","Negativecase"),
        ("Charlie", "Test1234$","Negativecase"),
    ],
    # Custom IDs for each test case
    ids=["Positive-case", "Negative-case", "Negative-case"]
)

def test_Orange_HRM_Login_Page_Error(playwright: Playwright,username, password,casetype) -> None:
        browser = playwright.webkit.launch(headless=False)
        page = browser.new_page()

        ## Open URL
        page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

        ## Enter details on login page (Positive & Negative)
        page.wait_for_selector('//input[@name="username"]').fill(username)
        page.wait_for_selector('//input[@name="password"]').fill(password)
        page.wait_for_selector('//button[@type="submit"]').click()

        ## Validation
        if casetype == "Positivecase":
           expect(page.get_by_text("Buzz Latest Posts")).to_be_visible()
        else:
           expect(page.get_by_text("Invalid credentials")).to_be_visible()
        print(username)
        print(password)
        print(casetype)

        ## Close browser
        browser.close()