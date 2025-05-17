from selenium.webdriver.remote.webdriver import WebDriver
import allure


class FirstPage:
    """
    Класс для инициации браузера и проверки url адреса
    """

    @allure.step("Запуск браузера")
    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://market-delivery.yandex.ru/"
        self.__driver = driver

    @allure.step("Переходим по ссылке в магазин")
    def go(self):
        self.__driver.get(self.__url)

    @allure.step("Проверяем URL")
    def get_current_url(self):
        return self.__driver.current_url
