Run payment_declined_test.py fot the test.

Test Description:
 
   The purpose of TC is check if trying to book tickets with incorrect credit card information will return
     payment declined error.
     1. login_to_main_page() - Run browser, open main page and maximize browser
     2. set_flight_information() - Login to main page using given user name and password
     3. set_booking_information() - Set all necessary information about flight - airports, tickets, date
     4. set_payment_information() - Select ticket according to class and price
     5. set_payment_information() - Set all payment information according to user and card - set incorrect credit card information
     6. check_if_payment_declined() - Try to book ticket with incorrect card information and wait for payment declined error.