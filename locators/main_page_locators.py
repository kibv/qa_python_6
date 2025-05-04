from selenium.webdriver.common.by import By

class MainPageLocators:
    FAQ_QUESTION = (By.ID, "accordion__heading-{}")
    FAQ_ANSWER = (By.ID, "accordion__panel-{}")

    ORDER_BUTTON_HEADER = (By.XPATH, "//div[contains(@class, 'Header_Nav__AGCXC')]//button[text()='Заказать']")
    ORDER_BUTTON_FOOTER = (By.XPATH, "//div[contains(@class, 'Home_FinishButton__1_cWm')]//button[text()='Заказать']")

    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    COOKIE_BANNER = (By.ID, "rcc-confirm-button")

