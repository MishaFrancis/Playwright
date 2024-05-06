from playwright.sync_api import expect,Playwright

class Person:
    def __init__(self, name, password):
        self.name = name
        self.password = password

people = [
    Person("Admin","admin123"),      ## Positive Data
    Person("Bob","Test1234$"),       ## Negative Data
    Person("Charlie","Test1234$")    ## Negative Data
]

def test_Orange_HRM_Login_Page_Error(playwright: Playwright) -> None:
    for person in people:
        browser = playwright.webkit.launch(headless=False)
        page = browser.new_page()

        ## Open URL
        page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

        ## Enter details on login page (Positive & Negative)
        page.wait_for_selector('//input[@name="username"]').fill(person.name)
        page.wait_for_selector('//input[@name="password"]').fill(person.password)
        page.wait_for_selector('//button[@type="submit"]').click()

        ## Validation
        if person.name == "Admin":
           expect(page.get_by_text("Buzz Latest Posts")).to_be_visible()
        else:
           expect(page.get_by_text("Invalid credentials")).to_be_visible()
        print(person.name)
        print(person.password)

        ## Close browser
        browser.close()