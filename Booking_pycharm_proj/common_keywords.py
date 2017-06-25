from test_common_variables import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
import time

common_wait_for_element_timeout = 15
common_check_if_element_visible_timeout = 5


# Finding elements

def get_element_by_xpath(driver, xpath, timeout=common_wait_for_element_timeout):
    '''
    Return webdriver element. If element is not visible during specified time, raise ElementNotVisibleException
    :param driver:
    :param xpath:
    :param timeout:
    :return:
    '''

    try:
        element = WebDriverWait(driver, timeout).until(lambda driver: driver.find_element_by_xpath(xpath))
        return element
    except TimeoutException:
        raise ElementNotVisibleException(
            "Component " + xpath + " could not be found during " + str(timeout) + " seconds!")


def get_element_by_name(driver, name, timeout=common_wait_for_element_timeout):
    '''
    Return webdriver element. If element is not visible during specified time, raise ElementNotVisibleException
    :param driver:
    :param name:
    :param timeout:
    :return:
    '''
    try:
        element = WebDriverWait(driver, timeout).until(lambda driver: driver.find_element_by_name(name))
        return element
    except TimeoutException:
        raise ElementNotVisibleException(
            "Component '" + name + "' could not be found during " + str(timeout) + " seconds!")


def get_element_by_text(driver, text, timeout=common_wait_for_element_timeout):
    '''
    Return webdriver element using text locator.
    :param driver:
    :param text:
    :param timeout:
    :return:
    '''
    element = WebDriverWait(driver, timeout).until(lambda driver: driver.find_elements_by_link_text(text))
    return element


def wait_until_element_is_clicable(driver, component_xpaht, timeout=common_wait_for_element_timeout):
    '''
    Checkin if component is clicable in specified time.
    :param driver:
    :param component_xpaht:
    :param timeout:
    :return:
    '''
    # TODO: check if this method is working as I would like to
    for i in range(5):
        component = get_element_by_xpath(driver, component_xpaht)
        if component.is_enabled():
            break
        else:
            time.sleep(2)


def check_if_component_is_visible(driver, component_xpaht, timeout=common_check_if_element_visible_timeout):
    '''
    Check if component is visible - using xpath. Return True/False
    :param driver:
    :param component_xpaht:
    :param timeout:
    :return:
    '''
    try:
        status = WebDriverWait(driver, timeout).until(lambda driver: driver.find_element_by_xpath(component_xpaht))
        return True
    except TimeoutException:
        return False


# Component evaluation

def click_on_component(driver, component_xpath):
    '''
    Click on component in specific sytuations - when component is not clicable and after some changes on page
    component star be clicable
    Flow:
    1. Click
    2. Wait for exceptions with text 'is not clickable at point'
    3. If there is no exceptions, break
    4. If there is any other exception - rise it
    5. if there is 'is not clickable at point' exception - wait 2 seconds and try agian

    :param driver:
    :param component_xpath:
    :return:
    '''
    time.sleep(3)
    component = get_element_by_xpath(driver, component_xpath)
    error_message = 'is not clickable at point'
    for i in range(5):
        try:
            component.click()
            break
        except Exception as e:
            error = str(e)
            if error_message in error:
                time.sleep(2)
            else:
                raise Exception(error)
    if i == 4:
        raise Exception(error)


def clear_text_field_and_insert(component, text):
    '''
    Get webdriver component - should be textfield then clear textfield and insert text
    :param component:
    :param text:
    :return:
    '''
    component.clear()
    component.send_keys(text)
