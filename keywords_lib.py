from element_locators import *
from common_variables_lib import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
import time

# Finding elements


def get_element_by_id(driver, id ,timeout=common_wait_for_element_timeout):
    element = WebDriverWait(driver, timeout).until(lambda driver: driver.find_element_by_id(id))
    return element


def get_element_by_xpath(driver, xpath ,timeout=common_wait_for_element_timeout):
    try:
        element = WebDriverWait(driver, timeout).until(lambda driver: driver.find_element_by_xpath(xpath))
        return element
    except TimeoutException:
        raise ElementNotVisibleException("Component " + xpath + " could not be found during " + str(timeout) +" seconds!" )

def get_element_by_name(driver, name ,timeout=common_wait_for_element_timeout):
    element = WebDriverWait(driver, timeout).until(lambda driver: driver.find_element_by_xpath(name))
    return element


def get_element_by_text(driver, text ,timeout=common_wait_for_element_timeout):
    print(type(driver))
    element = WebDriverWait(driver, timeout).until(lambda driver: driver.find_elements_by_link_text(text))
    return element


def wait_until_element_is_clicable(driver,component_xpaht,timeout=common_wait_for_element_timeout):

    #try:
    component = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, component_xpaht)))
    #except:
    #    pass


def check_if_component_is_visible(driver,component_xpaht,timeout=common_check_if_element_visible_timeout):
    try:
        status = WebDriverWait(driver, timeout).until(lambda driver: driver.find_element_by_xpath(component_xpaht))
        return True
    except TimeoutException:
        return False


# Component evaluation

def clear_text_field_and_insert(component,text):
    component.clear()
    component.send_keys(text)


def login_to_main_page(driver,username,password):
    print('login_to_main_page')

    login_link = get_element_by_xpath(driver,login_link_xpath)
    login_link.click()

    email_text_field_component = get_element_by_xpath(driver,email_address_text_field_xpath)
    clear_text_field_and_insert(email_text_field_component, username)

    password_text_field_component = get_element_by_xpath(driver,password_text_field_xpath)
    clear_text_field_and_insert(password_text_field_component, password)

    log_in_button_component = get_element_by_xpath(driver,log_in_button_xpath)
    log_in_button_component.click()


def select_one_way_flight(driver,radiobutton_xpath=one_way_flight_radio_button_xpath):
    print('select_one_way_flight')
    one_way_flight_radio_button_component = get_element_by_xpath(driver,radiobutton_xpath)
    wait_until_element_is_clicable(driver,radiobutton_xpath)
    time.sleep(2)
    one_way_flight_radio_button_component.click()


def select_aiport_city_from_pane_content(driver,aiport_city_name):
    print('select_aiport_city_from_pane_content')

    aiport_city_from_pane_content_xpath = "//*[@class='pane right']//*[contains(.,'"+aiport_city_name+"')]"
    print(aiport_city_from_pane_content_xpath)
    aiport_city_from_pane_content_component = get_element_by_xpath(driver,aiport_city_from_pane_content_xpath)
    aiport_city_from_pane_content_component.click()


def select_departure_and_destination(driver,departure_city_name,destination_city_name):
    print('select_departure_and_destination')
    departure_text_box_component = get_element_by_xpath(driver,departure_airport_text_box_xpath)
    wait_until_element_is_clicable(driver,departure_airport_text_box_xpath)
    departure_text_box_component.clear()
    departure_text_box_component.send_keys(departure_city_name)
    select_aiport_city_from_pane_content(driver,departure_city_name)

    destination_text_box_component = get_element_by_xpath(driver,destination_airport_text_box_xpath)
    wait_until_element_is_clicable(driver,destination_airport_text_box_xpath)
    destination_text_box_component.clear()
    destination_text_box_component.send_keys(destination_city_name)
    select_aiport_city_from_pane_content(driver, destination_city_name)


def accept_tickets(driver):
    print('accept_tickets')
    lets_go_button_component = get_element_by_xpath(driver, lets_go_button_xpath)
    wait_until_element_is_clicable(driver, lets_go_button_xpath)
    lets_go_button_component.click()


def select_first_available_date_from_calendar(driver):
    '''
    Handling calendar view:
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
    :return:
    '''
    print('select_first_available_date_from_calendar')

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

    '''
    for i in range(5):
        component_status = check_if_component_is_visible(driver,first_available_date_in_calendar_xpath)
        if component_status:
            date_component = get_element_by_xpath(driver, first_available_date_in_calendar_xpath)
            time.sleep(3)
            date_component.click()
            break
        else:
            arrow_right_component = get_element_by_xpath(driver,arrow_right_button_xpath)
            arrow_right_component.click()
    '''
