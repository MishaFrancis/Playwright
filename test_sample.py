from playwright.sync_api import sync_playwright

with sync_playwright() as m:

    browser = m.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    user_name = page.wait_for_selector('//input[@name="username"]')
    user_name.type('Admin')
    password = page.wait_for_selector('//input[@name="password"]')
    password.type('admin123')
    login_button = page.wait_for_selector('//button[@type="submit"]')
    login_button.click()
    page.wait_for_timeout(5000)
