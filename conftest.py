import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture
def driver():
    options = FirefoxOptions()
    options.headless = False
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

ORDER_DATA = [
    (
        "top",
        {
            "name": "Иван",
            "last_name": "Иванов",
            "address": "Москва, Красная площадь",
            "metro": "Лубянка",
            "phone": "+79991234567",
            "date": "01.01.2024",
            "rental_period": "сутки",
            "comment": "Тестовый заказ 1"
        }
    ),
    (
        "bottom",
        {
            "name": "Петр",
            "last_name": "Петров",
            "address": "Санкт-Петербург, Невский проспект",
            "metro": "Адмиралтейская",
            "phone": "+79997654321",
            "date": "31.12.2023",
            "rental_period": "двое суток",
            "comment": "Тестовый заказ 2"
        }
    )
]

FAQ_DATA = [
    (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
]