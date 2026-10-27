from playwright.sync_api import Page, expect
import re

def test_sortdropdown_locators(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    products=page.locator(".product-title")   # Matches with 6 products
 
    # 1 inner_text() vs text_content()

    # print("\n Inner text value :",products.nth(1).inner_text())
    # print("\n Text contents :",products.nth(1).text_content())

    # All the products with inner and text contents
    count=products.count()
    for i in range(count):
        print(products.nth(i).text_content().strip())
        # print(products.nth(i).inner_text())

    # Index all()
    product_locators=products.all()

    print(product_locators[0].inner_text())

    # for product_loc in product_locators:
    #     print(product_loc.inner_text())

    for i in range(len(product_locators)):
        print(product_locators[i].inner_text())
    
    page.wait_for_timeout(5000)

