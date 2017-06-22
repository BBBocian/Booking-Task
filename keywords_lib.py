from element_locators import *
from common_variables_lib import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Finding elements

def get_element_by_id(driver, id ,timeout=common_wait_for_element_timeout):
    element = WebDriverWait(driver, timeout).until(lambda driver: driver.find_element_by_id(id))
    return element


def get_element_by_xpath(driver, xpath ,timeout=common_wait_for_element_timeout):
    element = WebDriverWait(driver, timeout).until(lambda driver: driver.find_element_by_xpath(xpath))
    return element


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

def select_first_available_date_from_calendar(driver):
    print('select_first_available_date_from_calendar')

    button_arrow_right_component = get_element_by_xpath(driver,button_arrow_right_xpath)

    for i in range(10):
        wait_until_element_is_clicable(driver, button_arrow_right_xpath)

        try:
            date_component = get_element_by_xpath(driver, first_available_date_in_calendar_xpath,3)
        except TimeoutException as e:
            print(str(e))
        button_arrow_right_component.click()
        time.sleep(2)