from playwright.sync_api import Page, expect
import re

def test_sortdropdown_locators(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")


    # unsorted list
    

    unsorted_dropdown=page.locator("#colors>option")

    # sorted list

    # sorted_dropdown=page.locator("#animals>option")

    
       # scrolling down 
    page.mouse.wheel(0,500)

    option_text=[text.strip() for text in unsorted_dropdown.all_text_contents()]    # captured list

    orginal_list=option_text.copy()        # orginal list # copy of the main dropdown
    sorted_list=sorted(option_text)        # sorted list

    print("\n Orginal list :", orginal_list)
    print("\n Sorted list :", sorted_list)
    
    if orginal_list == sorted_list:
        print("\n Dropdown option are in sorted order")
        
    else:
        print("\n Dropdown option are not in sorted order")
           
    page.wait_for_timeout(3000)