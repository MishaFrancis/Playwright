from playwright.sync_api import sync_playwright, expect,Playwright
import re

class Person:
    def __init__(self, name, password):
        self.name = name
        self.password = password

people = [
    Person("Admin","admin123$"),
    Person("Bob","Test1234$"),
    Person("Charlie","Test1234$")
]

def test_Orange_HRM_Login_Page_Error(playwright: Playwright) -> None:
    for person in people:
        browser = playwright.webkit.launch(headless=True)
        page = browser.new_page()

        ## Open URL
        page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

        ## Enter details on login page
        page.wait_for_selector('//input[@name="username"]').fill(person.name)
        page.wait_for_selector('//input[@name="password"]').fill(person.password)
        page.wait_for_selector('//button[@type="submit"]').click()
        expect(page.get_by_text("Invalid credentials")).to_be_visible()
        print(person.name)
        print(person.password)

        ## Close browser
        browser.close()