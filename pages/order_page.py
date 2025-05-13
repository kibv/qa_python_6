from pages.base_page import BasePage
from locators import OrderPageLocators

class OrderPage(BasePage):
    def get_success_message(self):
        return self.find_element(OrderPageLocators.SUCCESS_TITLE).text

    def fill_first_step_form(self, user_data):
        self.fill_field(OrderPageLocators.NAME_FIELD, user_data['name'])
        self.fill_field(OrderPageLocators.LAST_NAME_FIELD, user_data['last_name'])
        self.fill_field(OrderPageLocators.ADDRESS_FIELD, user_data['address'])
        self.select_in_selector_metro_station(user_data['metro'])
        self.fill_field(OrderPageLocators.PHONE_FIELD, user_data['phone'])
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    def fill_second_step_form(self, user_data):
        self.input_text(OrderPageLocators.DATE_FIELD, user_data['date'])
        self.select_in_selector_rental_period(user_data['rental_period'])
        self.fill_field(OrderPageLocators.COMMENT_FIELD, user_data['comment'])
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

