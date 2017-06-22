__author__ = 'Szymon Krzemien'
from keywords_lib import *
from common_variables_lib import *
from selenium import webdriver
from selenium import *
import unittest

from selenium.webdriver.support.ui import WebDriverWait

class Booking(unittest.TestCase):

    def setUp(self):
       self.driver = webdriver.Chrome()
       self.driver.get("https://www.ryanair.com/ie/en/")
       self.driver.maximize_window()

    def test_check_declined_payment(self):
        driver = self.driver
        continue_button = get_element_by_text(driver,'Continue',common_element_timeout)
        continue_button.clear()
        continue_button.send_keys('Wroclaw')

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()