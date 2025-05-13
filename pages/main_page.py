from .base_page import BasePage
from locators import MainPageLocators
from data.data import URLS
import allure

class MainPage(BasePage):
    def click_order_top(self):
        self.click(MainPageLocators.ORDER_BUTTON_HEADER)

    def click_order_bottom(self):
        self.scroll_into_view(MainPageLocators.ORDER_BUTTON_FOOTER)
        self.click(MainPageLocators.ORDER_BUTTON_FOOTER)

    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    def click_order_button(self, position):
        if position == "top":
            order_button = self.wait_for_element(MainPageLocators.ORDER_BUTTON_HEADER)
        else:
            order_button = self.wait_for_element(MainPageLocators.ORDER_BUTTON_FOOTER)
        order_button.click()
    def redirect_to_dzen(self):
        main_window = self.get_current_window_handle()
        self.click_yandex_logo()
        self.switch_to_new_window(main_window, timeout=15)
        self.check_url_contains(URLS.DZEN_URL, timeout=20)
        return self.get_current_url().startswith(URLS.DZEN_URL)

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
        self.scroll_to_element(question_locator)
        self.scroll_to_element(question_locator)
        answer = self.wait_for_element(answer_locator)
        return question.text, answer.text

