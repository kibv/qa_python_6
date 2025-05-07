from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators
from data.data import URLS

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 15)

    def go_to_site(self):
        self.driver.get(URLS.BASE_URL)
        self.close_cookie_banner()

    def click_order_button(self, position):
        if position == "top":
            order_button = self.wait_for_element(MainPageLocators.ORDER_BUTTON_HEADER)
        else:
            order_button = self.wait_for_element(MainPageLocators.ORDER_BUTTON_FOOTER)
        order_button.click()

    def click_scooter_logo(self):
        scooter_logo = self.wait_for_element(MainPageLocators.SCOOTER_LOGO)
        scooter_logo.click()

    def click_yandex_logo(self):
        yandex_logo = self.wait_for_element(MainPageLocators.YANDEX_LOGO)
        yandex_logo.click()
    def redirect_to_dzen(self):
        main_window = self.driver.current_window_handle
        self.click_element(MainPageLocators.YANDEX_LOGO)
        self.switch_to_new_window(main_window, timeout=15)
        self.check_url_contains(URLS.DZEN_URL, timeout=20)
        return self.driver.current_url.startswith(URLS.DZEN_URL)



    def get_question_and_answer(self, index):
        question_locator = (
            MainPageLocators.FAQ_QUESTION[0],
            MainPageLocators.FAQ_QUESTION[1].format(index)
        )
        answer_locator = (
            MainPageLocators.FAQ_ANSWER[0],
            MainPageLocators.FAQ_ANSWER[1].format(index)
        )

        question = self.find_element(question_locator)
        self.scroll_to_element(question)
        question.click()
        self.scroll_to_element(question)
        answer = self.wait_for_element(answer_locator)
        return question.text, answer.text
