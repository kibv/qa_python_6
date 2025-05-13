from selenium.webdriver.common.by import By

class OrderPageLocators:
    COOKIE_BANNER = (By.ID, "rcc-confirm-button")
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[text()='* Срок аренды']")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    STATION_LOCATOR = lambda station: (By.XPATH, f"//div[text()='{station}']")
    RENTAL_LOCATOR = lambda period: (By.XPATH, f"//div[text()='{period}']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    PAGE_HEADER = (By.CLASS_NAME, 'Header_Header__3hI_1')
    STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and text()='Заказ оформлен']")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and text()='Ошибка']")
    SUCCESS_TITLE = (By.CSS_SELECTOR, "div.Order_ModalHeader__3FDaJ")