import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ecommerce-playground.lambdatest.io/")
    page.get_by_role("button", name=" My account").click()
    page.get_by_placeholder("E-Mail Address").click()
    page.get_by_placeholder("E-Mail Address").fill("narasimhulubuduru4822@gmail.com")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("Narasimhulu@12")
    page.get_by_role("button", name="Login").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
