from common_keywords import *
from test_element_locators import *
from selenium.webdriver.support.select import Select


def login_to_main_page(driver, username=login_username, password=login_password):
    '''
    Login to main page using given username and password
    :param driver:
    :param username:
    :param password:
    :return:
    '''
    login_link = get_element_by_xpath(driver, login_link_xpath)
    login_link.click()

    email_text_field_component = get_element_by_xpath(driver, email_address_text_field_xpath)
    clear_text_field_and_insert(email_text_field_component, username)

    password_text_field_component = get_element_by_xpath(driver, password_text_field_xpath)
    clear_text_field_and_insert(password_text_field_component, password)

    log_in_button_component = get_element_by_xpath(driver, log_in_button_xpath)
    log_in_button_component.click()


def select_one_way_flight(driver, radiobutton_xpath=one_way_flight_radio_button_xpath):
    '''
    Select radiobutton one way flight.
    :param driver:
    :param radiobutton_xpath:
    :return:
    '''
    one_way_flight_radio_button_component = get_element_by_xpath(driver, radiobutton_xpath)
    wait_until_element_is_clicable(driver, radiobutton_xpath)
    time.sleep(2)
    one_way_flight_radio_button_component.click()


def select_aiport_city_from_pane_content(driver, aiport_city_name):
    aiport_city_from_pane_content_xpath = "//*[@class='pane right']//*[contains(.,'" + aiport_city_name + "')]"
    aiport_city_from_pane_content_component = get_element_by_xpath(driver, aiport_city_from_pane_content_xpath)
    aiport_city_from_pane_content_component.click()


def select_departure_and_destination(driver, departure_city_name=departure_aiport,
                                     destination_city_name=destination_airport):
    '''
    Select departure and destinatnion aiport on main page - base on given arguments.
    :param driver:
    :param departure_city_name:
    :param destination_city_name:
    :return:
    '''
    departure_text_box_component = get_element_by_xpath(driver, departure_airport_text_box_xpath)
    wait_until_element_is_clicable(driver, departure_airport_text_box_xpath)
    departure_text_box_component.clear()
    departure_text_box_component.send_keys(departure_city_name)
    select_aiport_city_from_pane_content(driver, departure_city_name)

    destination_text_box_component = get_element_by_xpath(driver, destination_airport_text_box_xpath)
    wait_until_element_is_clicable(driver, destination_airport_text_box_xpath)
    destination_text_box_component.clear()
    destination_text_box_component.send_keys(destination_city_name)
    select_aiport_city_from_pane_content(driver, destination_city_name)


def accept_tickets(driver):
    '''
    Accept selested tickets by clicking "Let's go" button
    :param driver:
    :return:
    '''
    lets_go_button_component = get_element_by_xpath(driver, lets_go_button_xpath)
    wait_until_element_is_clicable(driver, lets_go_button_xpath)
    lets_go_button_component.click()


def select_first_available_date_from_calendar(driver):
    """Handling calendar view:
    First available day where flight is possible can be in next(than visible) months, that is why first
    checking if that available day (is visible) is execute.
    If any of days is not available --> select right arrow - show next month - and check one more time.
    To check how many month calendar has, simple comparison has been added.
    1. On the begining only 2 months are available on webpage (in html also)
    2. After clicking next month arrow - next month is adding to rest of months(in html)
    3. In every loop execution -
        a. check last month,
        b. click next month arrow and check last month again,
        c. if those months are the same - it means arrow right did not shown new month and calendar is out of scope
    :param driver:
    :return:"""
    condition = True
    while condition:
        month_name = driver.find_elements_by_xpath("//*[@id='row-dates-pax']//li[@class='calendar-view']//h1")
        last_month = month_name[-1].text

        component_status = check_if_component_is_visible(driver, first_available_date_in_calendar_xpath)
        if component_status:
            date_component = get_element_by_xpath(driver, first_available_date_in_calendar_xpath)
            time.sleep(1)
            date_component.click()
            condition = False
            break

        arrow_right_component = get_element_by_xpath(driver, arrow_right_button_xpath)
        arrow_right_component.click()
        time.sleep(1)

        current_month_name = driver.find_elements_by_xpath("//*[@id='row-dates-pax']//li[@class='calendar-view']//h1")
        current_last_month = current_month_name[-1].text
        time.sleep(1)

        if last_month == current_last_month:
            condition = False


def confirm_selected_aiports_and_tickets(driver):
    '''
    After selecting tickets, departure and destination aiports - click Let's go button to confirm
    If selected day is 'today' alert dialog with 'depart today' warning will appear - accept it
    :param driver:
    :return:
    '''
    lets_go_button_component = get_element_by_xpath(driver, lets_go_button_xpath)
    wait_until_element_is_clicable(driver, lets_go_button_xpath)
    lets_go_button_component.click()
    alert_dialog_depart_today_status = check_if_component_is_visible(driver, alert_depart_today_dialog_xpath)
    if alert_dialog_depart_today_status:
        alert_dialog_depart_today_ok_button_component = get_element_by_xpath(alert_depart_today_dialog_OK_button_xpath)
        alert_dialog_depart_today_ok_button_component.clikc()


def set_flight_information(driver):
    '''
    Set of functions to create flight preparation.
    1. Select radiobutton - one way flight
    2. Set departure and destination airports
    3. Select available date to book tickets
    4. Confirm all chooses by clicking button.
    :param driver:
    :return:
    '''
    select_one_way_flight(driver)
    select_departure_and_destination(driver, departure_aiport, destination_airport)
    select_first_available_date_from_calendar(driver)
    confirm_selected_aiports_and_tickets(driver)


def set_booking_information(driver):
    '''
    Set of steps to select available button and ticket class
    :param driver:
    :return:
    '''
    wait_until_element_is_clicable(driver, from_price_button_xpath)
    click_on_component(driver, from_price_button_xpath)

    wait_until_element_is_clicable(driver, standard_class_select_button_xpaht)
    click_on_component(driver, standard_class_select_button_xpaht)

    wait_until_element_is_clicable(driver, continue_booking_button_xpath)
    click_on_component(driver, continue_booking_button_xpath)

    wait_until_element_is_clicable(driver, checkout_booking_button_xpath)
    click_on_component(driver, checkout_booking_button_xpath)

    seat_prompt_popup_status = check_if_component_is_visible(driver, seat_prompt_popup_dialog_xpath)
    if seat_prompt_popup_status:
        seat_prompt_popup_dialog_ok_thanks_button_component = get_element_by_xpath(driver,
                                                                                   seat_prompt_popup_dialog_OK_thanks_button_xpath)
        seat_prompt_popup_dialog_ok_thanks_button_component.click()
    else:
        raise ElementNotVisibleException(
            "Component with locator " + seat_prompt_popup_dialog_xpath + " is not visible!")


def set_passenger_details(driver, passenger_title=user_title, first_name=user_first_name, last_name=user_last_name):
    '''
    set passenger information - first name, last name, and passenger title
    :param driver:
    :param passenger_title:
    :param first_name:
    :param last_name:
    :return:
    '''
    title_drop_down_component = get_element_by_xpath(driver, user_title_dropdown_xpath)
    Select(title_drop_down_component).select_by_visible_text(passenger_title)

    user_first_name_text_field_component = get_element_by_xpath(driver, user_first_name_text_field_xpath)
    clear_text_field_and_insert(user_first_name_text_field_component, user_first_name)

    user_last_name_text_field_component = get_element_by_xpath(driver, user_last_name_text_field_xpath)
    clear_text_field_and_insert(user_last_name_text_field_component, user_last_name)


def set_payment_and_contact_details(driver, country=user_country, mobile_number=user_mobile_number):
    user_country_dropdown_component = get_element_by_name(driver, user_country_drop_down_name)
    Select(user_country_dropdown_component).select_by_visible_text(country)

    user_mobile_number_text_field_component = get_element_by_xpath(driver, user_mobile_number_text_field_xpath)
    clear_text_field_and_insert(user_mobile_number_text_field_component, mobile_number)


def set_credit_card_information(driver, card_number=user_credit_card_number, card_type=user_credit_card_type,
                                month_expiry=user_credit_card_month_expiry, year_expiry=user_credit_card_year_expiry,
                                security_code=user_credit_card_secuirty_code, cardholders_name=user_cardholders_name):
    '''
    Set all necessary for booking credit card information
    :param driver:
    :param card_number:
    :param card_type:
    :param month_expiry:
    :param year_expiry:
    :param security_code:
    :param cardholders_name:
    :return:
    '''

    user_credit_card_number_text_field_component = get_element_by_name(driver, user_credit_card_number_text_field_name)
    clear_text_field_and_insert(user_credit_card_number_text_field_component, card_number)

    user_credit_card_type_dropdown_component = get_element_by_name(driver, user_credit_card_type_drop_down_name)
    Select(user_credit_card_type_dropdown_component).select_by_index(2)

    user_credit_card_month_expiry_dropdown_component = get_element_by_name(driver, user_credit_card_month_expiry_name)
    Select(user_credit_card_month_expiry_dropdown_component).select_by_visible_text(month_expiry)

    user_credit_card_year_expiry_drop_down_component = get_element_by_name(driver, user_credit_card_year_expiry_name)
    Select(user_credit_card_year_expiry_drop_down_component).select_by_visible_text(year_expiry)

    user_credit_card_secuirty_code_text_field_component = get_element_by_name(driver,
                                                                              user_credit_card_security_code_text_field_name)
    clear_text_field_and_insert(user_credit_card_secuirty_code_text_field_component, security_code)

    user_cardholders_name_text_field_component = get_element_by_xpath(driver,
                                                                      user_credit_card_holders_name_text_field_xpath)
    clear_text_field_and_insert(user_cardholders_name_text_field_component, cardholders_name)


def set_billing_address_information(driver, address1=user_address, city_name=user_city, postcode=user_post_code,
                                    country=user_country):
    user_billing_address1_text_field_component = get_element_by_name(driver, user_billing_address1_text_field_name)
    clear_text_field_and_insert(user_billing_address1_text_field_component, address1)

    user_billing_city_text_field_comonent = get_element_by_name(driver, user_billing_city_text_field_name)
    clear_text_field_and_insert(user_billing_city_text_field_comonent, city_name)

    user_billing_postcode_text_field_component = get_element_by_name(driver, user_billing_postcode_text_field_name)
    clear_text_field_and_insert(user_billing_postcode_text_field_component, postcode)

    user_billing_country_dropdown_component = get_element_by_name(driver, user_billing_country_dropdown_name)
    Select(user_billing_country_dropdown_component).select_by_visible_text(country)


def accept_policy_checkbox(driver):
    accept_policy_checkbox_component = get_element_by_name(driver, accept_policy_checkbox_name)
    accept_policy_checkbox_component.click()


def accept_payment(driver):
    pay_now_button_component = get_element_by_xpath(driver, pay_now_button_xpath)
    pay_now_button_component.click()


def check_if_payment_declined(driver):
    error_log_status = check_if_component_is_visible(driver, payment_declined_text_xpath, 10)
    if not error_log_status:
        raise Exception("Payment Declined error didn't appear!")
    else:
        print("Payment has been declined, test Passed.")


def set_payment_information(driver):
    '''
    set of keywords to handle payment information
    :param driver:
    :return:
    '''
    set_passenger_details(driver)
    set_payment_and_contact_details(driver)
    set_credit_card_information(driver)
    set_billing_address_information(driver)
    accept_policy_checkbox(driver)
    accept_payment(driver)
