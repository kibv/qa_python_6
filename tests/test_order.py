import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium.webdriver.support import expected_conditions as EC
from conftest import ORDER_DATA
@pytest.mark.usefixtures("driver")
@allure.feature("Order Tests")
class TestOrder:
    @pytest.mark.parametrize("position, user_data", ORDER_DATA)
    @allure.title("Test order flow from {position} button")
    def test_order_flow(self, driver, position, user_data):
        with allure.step("Open main page"):
            main_page = MainPage(driver)
            main_page.go_to_site()

        with allure.step(f"Click {position} order button"):
            main_page.click_order_button(position)

        with allure.step("Fill order form"):
            order_page = OrderPage(driver)
            order_page.fill_first_step_form(user_data)
            order_page.fill_second_step_form(user_data)

        with allure.step("Verify success message"):
            assert "Заказ оформлен" in order_page.get_success_message()

    @allure.title("Test Scooter logo redirect")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_scooter_logo()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title("Test Yandex logo redirect")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()

        main_window = driver.current_window_handle

        main_page.click_yandex_logo()

        WebDriverWait(driver, 15).until(lambda d: len(d.window_handles) > 1)
        new_window = [w for w in driver.window_handles if w != main_window][0]
        driver.switch_to.window(new_window)

        WebDriverWait(driver, 20).until(
            EC.url_contains("dzen.ru")
        )
        assert "dzen.ru" in driver.current_url