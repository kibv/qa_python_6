from .base_page import BasePage
from locators import OrderPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class OrderPage(BasePage):
    def fill_first_step_form(self, user_data):
        self.fill_field(OrderPageLocators.NAME_FIELD, user_data['name'])
        self.fill_field(OrderPageLocators.LAST_NAME_FIELD, user_data['last_name'])
        self.fill_field(OrderPageLocators.ADDRESS_FIELD, user_data['address'])
        self.select_metro_station(user_data['metro'])
        self.fill_field(OrderPageLocators.PHONE_FIELD, user_data['phone'])
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    def fill_second_step_form(self, user_data):
        self.fill_field(OrderPageLocators.DATE_FIELD, user_data['date'])
        self.select_rental_period(user_data['rental_period'])
        self.fill_field(OrderPageLocators.COMMENT_FIELD, user_data['comment'])
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    def fill_field(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def click_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
    def select_metro_station(self, station):
        self.close_cookie_banner()
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(OrderPageLocators.METRO_FIELD)
        ).click()

        station_locator = (By.XPATH, f"//div[text()='{station}']")
        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(station_locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def select_rental_period(self, period):
        self.close_cookie_banner()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD)
        ).click()

        period_locator = (By.XPATH, f"//div[text()='{period}']")
        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(period_locator)
        )
        self.driver.execute_script("arguments[0].click();", element)