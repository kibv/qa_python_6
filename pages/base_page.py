from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
import time
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_field(self, locator, text, timeout=5):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        self.driver.find_element(*OrderPageLocators.DATE_FIELD).send_keys(Keys.ESCAPE)

    def select_in_selector_metro_station(self, station):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(OrderPageLocators.METRO_FIELD)).click()
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(OrderPageLocators.STATION_LOCATOR(station)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
    def select_in_selector_rental_period(self, period):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD)).click()
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(OrderPageLocators.RENTAL_LOCATOR(period)))
        self.driver.execute_script("arguments[0].click();", element)
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.3)

    def click_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()

    def wait_for_new_window(self, url, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) > 1)
    def switch_to_new_window(self, main_window, timeout=10):
        self.wait_for_new_window(timeout)
        new_window = [w for w in self.driver.window_handles if w != main_window][0]
        self.driver.switch_to.window(new_window)

    def check_url_contains(self, expected_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(expected_url))

    def close_cookie_banner(self):
        try:
            cookie_btn = self.wait_for_element(OrderPageLocators.COOKIE_BANNER, 1)
            cookie_btn.click()
        except TimeoutException:
            print("Cookie banner not found or not clickable")

    def find_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text.strip()

