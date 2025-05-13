import allure
import pytest
from pages.main_page import MainPage
from data.data import FAQ_DATA, URLS
@pytest.mark.usefixtures("driver")
@allure.feature("FAQ Tests")
class TestFAQ:
    @allure.title("Test FAQ question {index}, {expected_question}, {expected_answer}")
    @pytest.mark.parametrize("index, expected_question, expected_answer", FAQ_DATA)
    def test_faq_item(self, driver, index, expected_question, expected_answer):
        with allure.step("Open main page"):
            main_page = MainPage(driver)
            main_page.open(URLS.BASE_URL)
        with allure.step(f"Click question {index}: {expected_question}, {expected_answer}"):
            actual_question, actual_answer = main_page.get_question_and_answer(index)
            assert actual_question == expected_question, f"Текст вопроса не совпадает для элемента #{index}"
            assert actual_answer == expected_answer, f"Текст ответа не совпадает для элемента #{index}"
