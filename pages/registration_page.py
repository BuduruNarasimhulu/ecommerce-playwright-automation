import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=2000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ecommerce-playground.lambdatest.io/")
    page.get_by_role("button", name=" My account").click()
    page.get_by_role("link", name="Continue").click()
    page.get_by_placeholder("First Name").click()
    page.get_by_placeholder("First Name").fill("narasimhulu")
    page.get_by_placeholder("Last Name").click()
    page.get_by_placeholder("Last Name").fill("buduru")
    page.get_by_placeholder("E-Mail").click()
    page.get_by_placeholder("E-Mail").fill("narasimhulubuduru4822@gmail.com")
    page.get_by_placeholder("Telephone").click()
    page.get_by_placeholder("Telephone").fill("+91 6303759197")
    page.get_by_placeholder("Password", exact=True).click()
    page.get_by_placeholder("Password", exact=True).fill("Narasimhulu@12")
    page.get_by_placeholder("Password Confirm").click()
    page.get_by_placeholder("Password Confirm").fill("Narasimhulu@12")
    page.get_by_text("I have read and agree to the").click()
    page.get_by_role("button", name="Continue").click()
   

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)




