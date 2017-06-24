from test_keywords import *
from selenium import webdriver
import unittest

__author__ = 'Szymon Krzemien'


class Booking(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.ryanair.com/ie/en/")
        self.driver.maximize_window()

    def test_check_declined_payment(self):
        driver = self.driver

        login_to_main_page(driver)

        set_flight_information(driver)

        set_booking_information(driver)

        set_payment_information(driver)

        check_if_payment_declined(driver)


    def tearDown(self):
        self.driver.close()
        pass


if __name__ == '__main__':
    unittest.main()
