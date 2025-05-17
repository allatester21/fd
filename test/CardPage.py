import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CardPage:
    """
    Класс для работы с товарами в корзине
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализируем драйвер браузера
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.__driver = driver

    @allure.step("Выбор товара")
    def store_selection(self):
        self.__driver.find_element(
            By.CSS_SELECTOR, '[data-testid="place-header-root"]').click()

    @allure.step("Добавление товара в корзину")
    def add_product(self):
        """
        Ожидаем появление результата поиска
        """
        WebDriverWait(self.__driver, 4).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, '[data-testid="search-results-title"]')))

        """
        Увеличение товара в корзине до 5 штук
        """
        self.__driver.find_element(
            By.CSS_SELECTOR, 'button.b17t8bbz.o31qs5d').click()
        add_button = self.__driver.find_element(
            By.CSS_SELECTOR, '[data-testid="amount-select-increment"]')
        for _ in range(5):
            add_button.click()
            time.sleep(1)  # Пауза, чтобы увидеть результат

    @allure.step("Очистка корзины")
    def clear_checkout(self):
        self.__driver.find_element(
            By.CSS_SELECTOR, '[data-testid="cart-clear-button"]').click()
        time.sleep(2)
        self.__driver.find_element(
            By.CSS_SELECTOR, 'button.r1orm7zp.st0n1t4.v102ekr4.shkwuuz.UiKitConfirmModal_confirm.UiKitConfirmModal_buttonContent.UiKitConfirmModal_textAlign').click()
        time.sleep(2)
