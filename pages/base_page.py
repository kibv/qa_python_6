from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def open(self, url: str):
        self.driver.get(url)
        self.close_cookie_banner()

    def find(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )
    def find_all(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def scroll_into_view(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def fill_field(self, locator, text, timeout=10):
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

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def scroll_to_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        self.execute_script("""
                document.body.style.scrollBehavior = 'auto';
                arguments[0].scrollIntoView({behavior: 'auto', block: 'start'});
                window.scrollBy(0, -500);
            """, element)
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.execute_script("arguments[0].click();", element)


    def click_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()

    def get_current_window_handle(self):
        return self.driver.current_window_handle
    def wait_for_new_window(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) > 1)

    def switch_to_new_window(self, original_window, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > 1
        )
        for window in self.driver.window_handles:
            if window != original_window:
                self.driver.switch_to.window(window)
                break

    def check_url_contains(self, expected_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(expected_url))

    def close_cookie_banner(self):
        try:
            cookie_btn = self.wait_for_element(OrderPageLocators.COOKIE_BANNER, 1)
            cookie_btn.click()
        except TimeoutException:
            print("Cookie banner not found or not clickable")

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text.strip()

    def get_current_url(self):
        return self.driver.current_url
