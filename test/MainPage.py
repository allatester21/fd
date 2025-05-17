import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    """
    Класс для внесения адреса доставки и поиска продукта
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализируем драйвер браузера
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.__driver = driver

    @allure.step("Указываем адрес доставки")
    def add_address(self, address) -> str:
        self.__driver.find_element(
            By.XPATH, '//span[text()="Укажите адрес доставки"]').click()
        self.__driver.find_element(
            By.CSS_SELECTOR, "input.afdxd29.mr7w3hr").send_keys(address)
        self.__driver.find_element(
            By.XPATH, '//span[text()="ОК"]').click()
        response = self.__driver.find_element(
            By.CSS_SELECTOR, 'span.a1a8ol1h').text
        return (response)

    @allure.step("Вводим название продукта в поле поиска в верхнем левом углу")
    def open_find(self, product: str):
        self.__driver.find_element(By.ID, "id_1").send_keys(product)
        self.__driver.find_element(
            By.CSS_SELECTOR, 'button.r1jyb6b1.slw94yn.v102ekr4.syv67cr.UIInputAction_root').click()

        """
        Ожидаем появление результата поиска
        """
        WebDriverWait(self.__driver, 4).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h1'))
        )
