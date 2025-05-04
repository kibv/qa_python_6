import allure
import pytest
from pages.main_page import MainPage
from conftest import FAQ_DATA
@pytest.mark.usefixtures("driver")
@allure.feature("FAQ Tests")
class TestFAQ:
    @pytest.mark.parametrize("index, expected", FAQ_DATA)
    @allure.title("Test FAQ question {index}")
    def test_faq_question(self, driver, index, expected):
        with allure.step("Open main page"):
            main_page = MainPage(driver)
            main_page.go_to_site()

        with allure.step(f"Click question {index}"):
            main_page.click_faq_question(index)

        with allure.step("Verify answer text"):
            assert main_page.get_faq_answer_text(index) == expected