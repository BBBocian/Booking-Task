cookie_popup_xpaht = "//*[@class='cookie-popup']"
closing_cookie_popup_button_xpath = "//*[@class='close-icon']"

# login dialog locators
login_link_xpath = "//*[@id='myryanair-auth-login']//a"
email_address_text_field_xpath = "//*[@class='signup-modal']//*[@name='emailAddress']"
password_text_field_xpath = "//*[@class='signup-modal']//*[@name='password']"
log_in_button_xpath = "//*[@class='signup-modal']//*[@class='core-btn-primary']"

# selecting flight details locators
one_way_flight_radio_button_xpath = "//*[@id='search-container']//*[@id='lbl-flight-search-type-one-way']"
departure_airport_text_box_xpath = "//*[@id='search-container']//*[@class='col-departure-airport']//input[@role='textbox']"
destination_airport_text_box_xpath = "//*[@id='search-container']//*[@class='col-destination-airport']//input[@role='textbox']"
start_date_calendar_xpath = "//*[@class='start_date']"
arrow_right_button_xpath = "//button[@class='arrow right']"
arrow_left_button_xpath = "//button[@class='arrow left']"
lets_go_button_xpath = "//*[@translate='common.buttons.lets_go']"
first_available_date_in_calendar_xpath = "//*[@id='row-dates-pax']//li[not(@class) and @ng-if='!range']"

# selecting tickets details locators
from_price_button_xpath = "//*[contains(@class,'flight-header__min-price')]//*[@class='core-btn-primary']"
alert_depart_today_dialog_xpath = "//div[@role='alertdialog]//*[contains(.,'departs_today')]'"
alert_depart_today_dialog_OK_button_xpath = "//div[@role='alertdialog]//*[contains(.,'OK')]'"
standard_class_select_button_xpaht = "//*[@class='ranimate-flight-fares']//*[contains(@class,'standard')]//button[@id='continue']"
leisure_class_select_button_xpaht = "//*[@class='ranimate-flight-fares']//*[contains(@class,'leisure')]//button[@id='continue']"
business_class_select_button_xpaht = "//*[@class='ranimate-flight-fares']//*[contains(@class,'business')]//button[@id='continue']"
continue_booking_button_xpath = "//*[@id='booking-selection']//*[@translate='trips.summary.buttons.btn_continue']"
checkout_booking_button_xpath = "//*[@id='booking-selection']//*[@translate='trips.summary.buttons.btn_checkout']"
seat_prompt_popup_dialog_xpath = "//*[@class='seat-prompt-popup']"
seat_prompt_popup_dialog_OK_thanks_button_xpath = "//*[@class='seat-prompt-popup']//*[@translate='trips.summary.seat.prompt.popup.reject']"

# Passenger details locators
user_first_name_text_field_xpath = "//input[contains(@id,'firstName')]"
user_last_name_text_field_xpath = "//input[contains(@id,'lastName')]"
user_title_dropdown_xpath = "//select[contains(@name,'title')]"

# Payment and contact details locators

user_country_drop_down_name = "phoneNumberCountry"
user_mobile_number_text_field_xpath = "//input[@name='phoneNumber']"

# Payment method locators
user_credit_card_number_text_field_name = "cardNumber"
user_credit_card_type_drop_down_name = "cardType"
user_credit_card_month_expiry_name = "expiryMonth"
user_credit_card_year_expiry_name = "expiryYear"
user_credit_card_security_code_text_field_name = "securityCode"
user_credit_card_holders_name_text_field_xpath = "//input[@name='cardHolderName']"

# Billing address locators
user_billing_address1_text_field_name = "billingAddressAddressLine1"
user_billing_city_text_field_name = "billingAddressCity"
user_billing_postcode_text_field_name = "billingAddressPostcode"
user_billing_country_dropdown_name = "billingAddressCountry"

# accept policy locator
accept_policy_checkbox_name = "acceptPolicy"

# pay now button locator
pay_now_button_xpath = "//*[@translate='common.components.payment_forms.pay_now']"

# Payment Declined element locator

payment_declined_text_xpath = "//prompt[contains(@ng-switch-when,'PaymentDeclined')]//*[contains(.,'payment was not authorised')]"
