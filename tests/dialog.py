from playwright.sync_api import Page, expect
import re
import pytest

@pytest.mark.skip
def test_simple_dialog(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

     # scrolling down 
    page.mouse.wheel(0,500)
    
    # Scenario 1
    # register the event

    def handle_dialog(dialog):
        dialog.accept()
    
    page.on("dialog", handle_dialog)  

    # page.wait_for_timeout(5000)

    page.locator("#alertBtn").click()

    page.wait_for_timeout(5000)

    
@pytest.mark.skip   
def test_lambada_dialog(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

     # scrolling down 
    page.mouse.wheel(0,500)
    
    # Scenario 2   ---> Most pefferable

    # register the event

    page.on("dialog", lambda dialog:dialog.accept() )  # lambda parameters : expression

    page.wait_for_timeout(3000)

    page.locator("#alertBtn").click()

    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_confrm_dialog(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

     # scrolling down 
    page.mouse.wheel(0,500)
    
    # register the event

    page.on("dialog", lambda dialog:dialog.accept() )  # lambda parameters : expression

    page.wait_for_timeout(3000)

    page.locator("#confirmBtn").click()

    page.wait_for_timeout(5000)

    text=page.locator("#demo").inner_text()
    print("Output text : ===>", text)

    expect(page.locator("#demo")).to_have_text("You pressed OK!")

@pytest.mark.skip
def test_dismiss_dialog(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

     # scrolling down 
    page.mouse.wheel(0,500)
    
    # register the event

    page.on("dialog", lambda dialog:dialog.dismiss() )  # lambda parameters : expression

    page.wait_for_timeout(3000)

    page.locator("#confirmBtn").click()

    page.wait_for_timeout(5000)

    text=page.locator("#demo").inner_text()
    print("Output text : ===>", text)

    expect(page.locator("#demo")).to_have_text("You pressed Cancel!")

#@pytest.mark.skip
def test_prompt_dialog(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

     # scrolling down 
    page.mouse.wheel(0,500)
    
    # register the event

    page.on("dialog", lambda dialog:dialog.accept("John"))  # lambda parameters : expression

    page.wait_for_timeout(3000)

    page.locator("#promptBtn").click()

    page.wait_for_timeout(5000)

    text=page.locator("#demo").inner_text()
    print("Output text : ===>", text)

    expect(page.locator("#demo")).to_have_text("Hello John! How are you today?")