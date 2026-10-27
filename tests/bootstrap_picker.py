from playwright.sync_api import Page, expect
import re


def select_checkin_date(page, year , month, day):
    while True:
        checkin_month_year=page.locator("h3[aria-live='polite']").nth(0).inner_text()
        current_month, current_year=checkin_month_year.split(" ")
        if current_month == month and current_year == year:
            break
        else:
            page.locator("button[aria-label='Next month']").click()

    all_dates=page.locator("table.b8fcb0c66a tbody").nth(0).locator("td").all()

    for date in all_dates:
        if date.inner_text() == day:
            date.click()
            break
            
            
def select_checkout_date(page, year, month, day):
    while True:
        checkout_month_year=page.locator("h3[aria-live='polite']").nth(1).inner_text()
        current_month, current_year=checkout_month_year.split(" ")
        if current_month == month and current_year == year:
            break
        else:
            page.locator("button[aria-label='Next month']").click()

    all_dates=page.locator("table.b8fcb0c66a tbody").nth(1).locator("td").all()

    for date in all_dates:
        if date.inner_text() == day:
            date.click()
            break


def test_booking_picker(page: Page):
    page.goto("https://www.booking.com")

    page.wait_for_timeout(2000)
    page.get_by_test_id("searchbox-dates-container").click()
    
    select_checkin_date(page, "2026", "March", "18")
    select_checkout_date(page, "2026", "April", "20")

    check_in=page.get_by_test_id("date-display-field-start").inner_text()
    check_out=page.get_by_test_id("date-display-field-end").inner_text()

    print("\n Check in date ----->", check_in)
    print("\n Check out date ----->", check_out)

    expect(page.get_by_test_id("date-display-field-start")).to_contain_text(check_in)
    expect(page.get_by_test_id("date-display-field-end")).to_contain_text(check_out)
    
    page.wait_for_timeout(5000)

    



