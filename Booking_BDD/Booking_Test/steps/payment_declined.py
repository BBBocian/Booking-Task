from behave import given,when,then
from data.test_keywords import *

@given("I navigate my browser to main page")
def open_browser_and_go_to_main_page(context):

    context.browser.get(web_page_link)
    context.browser.maximize_window()


@when("I'm trying to book ticket with incorrect credit card number")
def book_ticket_with_incorrect_card_number(context):

    check_if_cookie_popup_exist(context.browser)

    login_to_main_page(context.browser)

    set_flight_information(context.browser)

    set_booking_information(context.browser)

    set_payment_information(context.browser)


@then("I'm getting the message about payment declined")
def check_if_payment_has_been_declined(context):
    check_if_payment_declined(context.browser)

