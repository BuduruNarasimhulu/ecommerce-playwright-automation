import re
from playwright.sync_api import Playwright, sync_playwright, expect, TimeoutError as PlaywrightTimeoutError

def select_category(page, category_name):
    """Select a category from the 'All Categories' dropdown."""
    try:
        # Wait for the dropdown button to be visible and then click it
        page.wait_for_selector("button[aria-label='All Categories']", timeout=10000)
        page.get_by_role("button", name="All Categories").click()
        page.get_by_role("link", name=category_name, exact=True).click()
        print(f"Selected category: {category_name}")
    except PlaywrightTimeoutError:
        print(f"Failed to select category '{category_name}' - button not visible.")

def search_product(page, product_name):
    """Search for a product by name."""
    search_box = page.get_by_role("textbox", name="Search For Products")
    search_box.click()
    search_box.fill(product_name)
    page.get_by_role("button", name="Search").click()
    print(f"Searched for product: {product_name}")

def click_product_from_search(page, product_name):
    """Click on a product from the search results."""
    try:
        page.get_by_text(product_name).first.click()
        print(f"Clicked on product: {product_name}")
    except PlaywrightTimeoutError:
        print(f"Product '{product_name}' not found in search results.")

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # Navigate to the homepage
    page.goto("https://ecommerce-playground.lambdatest.io/index.php?route=common/home")
    
    # Test Dropdown Categories and Search
    categories_to_test = [
        {"category": "Desktops", "search_term": "ap", "product_name": "Apple Cinema 30\""},
        {"category": "Laptops", "search_term": "laptops", "product_name": "No Product Expected"},  # No product should be found
        {"category": "Components", "search_term": "sam", "product_name": "Samsung SyncMaster 941BW"},
        {"category": "Tablets", "search_term": "m", "product_name": "Palm Treo Pro"},
        {"category": "Software", "search_term": "mac", "product_name": "iMac"},
        {"category": "Phones & PDAs", "search_term": "ipho", "product_name": "iPhone"},
        {"category": "Cameras", "search_term": "ip", "product_name": "iPod Classic"},
        {"category": "MP3 Players", "search_term": "sa", "product_name": "Samsung Galaxy Tab"},
    ]

    for item in categories_to_test:
        # Select the category from the dropdown
        select_category(page, item["category"])
        
        # Search for the product
        search_product(page, item["search_term"])

        # Handle special case for no product found
        if item["product_name"] == "No Product Expected":
            try:
                expect(page.get_by_text("There is no product that")).to_be_visible(timeout=5000)
                print(f"No products found for search term '{item['search_term']}' as expected.")
                page.get_by_role("link", name="Continue").click()
            except PlaywrightTimeoutError:
                print("Expected 'No products found' message but didn't see it.")
        else:
            # Click on the product from the search results if found
            click_product_from_search(page, item["product_name"])

    # Close the browser
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)



