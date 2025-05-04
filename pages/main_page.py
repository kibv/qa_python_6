from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    def close_cookie_banner(self):
        try:
            cookie_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(MainPageLocators.COOKIE_BANNER)
            )
            cookie_btn.click()
        except:
            pass

    def click_scooter_logo(self):
        self.close_cookie_banner()
        logo = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.SCOOTER_LOGO)
        )
        logo.click()

    def click_yandex_logo(self):
        self.close_cookie_banner()
        logo = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.YANDEX_LOGO)
        )
        logo.click()

    def click_faq_question(self, index):
        self.close_cookie_banner()
        question_locator = (MainPageLocators.FAQ_QUESTION[0],
                            MainPageLocators.FAQ_QUESTION[1].format(index))
        question = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(question_locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", question)
        self.driver.execute_script("arguments[0].click();", question)

    def click_order_button(self, position):
        self.close_cookie_banner()
        locator = (MainPageLocators.ORDER_BUTTON_HEADER if position == "top"
                   else MainPageLocators.ORDER_BUTTON_FOOTER)
        button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].click();", button)

    def get_faq_answer_text(self, index):
        answer_locator = (
            MainPageLocators.FAQ_ANSWER[0],
            MainPageLocators.FAQ_ANSWER[1].format(index)
        )
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(answer_locator)
        ).text