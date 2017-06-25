# Booking-Task
Draft version created in selenium webdriver + python. Selenium + python has been choosen because this is the best start to improve TC in BDD way. Test in BDD has been created but not in the form I would like to present.

Test information: 

The purpose of TC is check if trying to book tickets with incorrect credit card information will return
     payment declined error.
     
     0. check_if_cookie_popup_exist() - check if cookies popup exist
     
     1. login_to_main_page() - Run browser, open main page and maximize browser
     
     2. set_flight_information() - Login to main page using given user name and password
     
     3. set_booking_information() - Set all necessary information about flight - airports, tickets, date
     
     4. set_payment_information() - Select ticket according to class and price
     
     5. set_payment_information() - Set all payment information according to user and card - set incorrect credit card information
     
     6. check_if_payment_declined() - Try to book ticket with incorrect card information and wait for payment declined error.
     
Use payment_declined_test.py to run project.      
     
Pycharm project can be used as well as run python file from Separated_files folder. Go to Separated_files direcotry and execute python payment_declined_test.py 
If gecodriver or chrome dirver are missing, add Separated_files dir to your PATH.

Tested on Firefox/Chrome.

Test is multilanguage - be aware of that for other languaes some component values are different e.g. Names of Cities or person titles.
All different names can be changed in test_common_variables.py - this could be improvement by property files.

There is no sophisticated log system. If test passed only information about it is displaying. 
