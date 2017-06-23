__author__ = 'Szymon Krzemien'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from keywords_lib import *
from element_locators import *
from common_variables_lib import *
import unittest
from threading import Thread
import time


from selenium.webdriver.support.ui import WebDriverWait

class Booking(unittest.TestCase):

    def setUp(self):
       self.driver = webdriver.Chrome()
       self.driver.get("https://www.ryanair.com/ie/en/")
       self.driver.maximize_window()

    def test_check_declined_payment(self):

        login_username = 'szymciunio@gmail.com'
        login_password = 'Alamakota123'
        departure_aiport = 'Wroclaw'
        destination_aiport = 'Lisbon'

        driver = self.driver



        login_to_main_page(driver, login_username, login_password)

        select_one_way_flight(driver)

        select_departure_and_destination(driver, departure_aiport, destination_aiport)

        select_first_available_date_from_calendar(driver)

        lets_go_button_component = get_element_by_xpath(driver,lets_go_button_xpath)
        wait_until_element_is_clicable(driver,lets_go_button_xpath)
        lets_go_button_component.click()


    def tearDown(self):
        #self.driver.close()
        pass

if __name__ == '__main__':
    unittest.main()