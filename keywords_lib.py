from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def get_element_by_id(driver, id ,timeout):
    driver = WebDriverWait(driver, timeout).until(lambda driver: driver.find_element_by_id(id))
    return driver

def get_element_by_xpath(driver, xpath ,timeout):
    driver = WebDriverWait(driver, timeout).until(lambda driver: driver.find_element_by_xpath(xpath))
    return driver

def get_element_by_name(driver, name ,timeout):
    driver = WebDriverWait(driver, timeout).until(lambda driver: driver.find_element_by_xpath(name))
    return driver

def get_element_by_text(driver, text ,timeout):
    driver = WebDriverWait(driver, timeout).until(lambda driver: driver.find_elements_by_link_text(text))
    return driver

