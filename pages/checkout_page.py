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

    
    # Navigate and add items to the cart
    page.get_by_role("button", name="Shop by Category").click()
    page.locator("#widget-navbar-217841").get_by_role("link", name="Components").click()
    page.get_by_role("link", name="HTC Touch HD", exact=True).click()
    page.get_by_role("button", name="Add to Cart").click()
    page.get_by_role("link", name="View Cart ").click()
    page.get_by_role("link", name="Checkout").click()
    
    # Checkout process
    page.locator("#payment-address").get_by_text("I want to use a new address").click()
    page.get_by_role("textbox", name="First Name*").click()
    page.get_by_role("textbox", name="First Name*").fill("Narasimhulu")
    page.get_by_role("textbox", name="Last Name*").click()
    page.get_by_role("textbox", name="Last Name*").fill("buduru")
    page.get_by_role("textbox", name="Company").click()
    page.get_by_role("textbox", name="Company").fill("accion labs")
    page.get_by_role("textbox", name="Address 1*").click()
    page.get_by_role("textbox", name="Address 1*").fill("Benglore")
    page.get_by_role("textbox", name="Address 2").click()
    page.get_by_role("textbox", name="City*").click()
    page.get_by_role("textbox", name="City*").fill("Bengaluru")
    page.get_by_text("I have read and agree to the Terms & Conditions").click()
    page.get_by_role("button", name="Continue ").click()
    page.get_by_role("heading", name="Confirm Order").click()
    page.get_by_role("button", name="Confirm Order ").click()
    page.get_by_role("heading", name="Your order has been placed!").click()
    page.get_by_text("Your order has been successfully processed!").click()
    page.get_by_text("Thanks for shopping with us").click()

    # Close browser context
    context.close()
    browser.close()

# Run the Playwright script
with sync_playwright() as playwright:
    run(playwright)


