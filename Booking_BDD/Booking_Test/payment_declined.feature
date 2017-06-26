# Created by Szymon Krzemien at 26.06.2017
Feature: Testing payment declined
  # Enter feature description here

  Scenario: Payment declined during booking ticket
  #  STEPS:
  #  0. Run browser, open main page and maximize browser
  #  1. Check if cookies popup exist
  #  2. Login to main page using given user name and password
  #  3. Set all necessary information about flight - airports, tickets, date
  #  4. Select ticket according to class and price
  #  5. Set all payment information according to user and card - set incorrect credit card information
  #  6. Try to book ticket with incorrect card information and wait for payment declined error.\
    Given I navigate my browser to main page
    When I'm trying to book ticket with incorrect credit card number
    Then I'm getting the message about payment declined