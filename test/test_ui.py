import time
import allure
from selenium.webdriver.common.by import By
from FirstPage import FirstPage
from MainPage import MainPage
from CardPage import CardPage


@allure.suite("Тестирование магазина")
@allure.title("Проверка адреса сайта delivery")
@allure.description("Тест проверяет загрузку страницы сайта delivery")
@allure.feature("Адрес сайта досавки")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    first_page = FirstPage(driver)
    first_page.go()
    time.sleep(20)   # Исключаем появление запроса "Вы робот?"

    with allure.step("Проверяем, что URL заканчивается на shippingType=delivery"):
        current_url = first_page.get_current_url()
        assert current_url.endswith("shippingType=delivery"), (
            f"URL должен заканчиваться на shippingType=delivery, "
            f"фактический URL: {current_url}")


@allure.suite("Тестирование магазина")
@allure.title("Проверка правильности ввода адреса доставки")
@allure.description("Тест проверяет правильность отображения "
                    "адреса доставки на странице магазина.")
@allure.feature("Адрес доставки")
@allure.severity(allure.severity_level.MINOR)
def test_add_address(driver):
    with allure.step("Загрузка браузера"):
        first_page = FirstPage(driver)
        first_page.go()
        time.sleep(5)   # Исключаем появление запроса "Вы робот?"

    with allure.step("Вносим адрес доставки"):
        main_page = MainPage(driver)
        address = "Большой Дровяной переулок, 10, Москва\n"
        address_view = "Большой Дровяной переулок\n, 10"
        result_address = main_page.add_address(address)
        time.sleep(2)

    with allure.step("Проверка отображаемого адреса"):
        assert result_address in address_view, (
            f"Введенный адрес '{result_address}' "
            f"совпадает с ожидаемым '{address_view}'")


@allure.suite("Тестирование магазина")
@allure.title("Проверка поиска продуктов")
@allure.description("Тест проверяет работу поиска продуктов в магазине.")
@allure.feature("Поиск продуктов")
@allure.severity(allure.severity_level.MINOR)
def test_search_products(driver):
    with allure.step("Загрузка браузера"):
        first_page = FirstPage(driver)
        first_page.go()
        time.sleep(5)   # Исключаем появление запроса "Вы робот?"

    with allure.step("Вносим адрес доставки"):
        main_page = MainPage(driver)
        address = "Большой Дровяной переулок, 10, Москва\n"
        main_page.add_address(address)
        time.sleep(2)

    with allure.step("Поиск прдуктов"):
        product = "молоко"
        main_page.open_find(product)

    with allure.step("Проверка наличия результатов поиска"):
        find_element = driver.find_element(By.CSS_SELECTOR, 'h1')
        text_array = find_element.text.split(" ")

        assert int(text_array[1]) > 0, (f"Количество найденных "
                                        f"продуктов: {int(text_array[1])}")


@allure.suite("Тестирование магазина")
@allure.title("Проверка выбора и добавления товара в корзину")
@allure.description("Тест проверяет выбор товара и его добавление в корзину.")
@allure.feature("Выбор и добавление товара")
@allure.severity(allure.severity_level.CRITICAL)
def test_select_and_add_product(driver):
    with allure.step("Загрузка браузера"):
        first_page = FirstPage(driver)
        first_page.go()
        time.sleep(15)  # Исключаем появление запроса "Вы робот?"

    with allure.step("Вносим адрес доставки"):
        main_page = MainPage(driver)
        address = "Большой Дровяной переулок, 10, Москва\n"
        main_page.add_address(address)
        time.sleep(2)

    with allure.step("Поиск прдуктов"):
        product = "молоко"
        main_page.open_find(product)

    with allure.step("Выбираем товар"):
        card_page = CardPage(driver)
        card_page.store_selection()

    with allure.step("Переход в новую вкладку"):
        windows_handles = driver.window_handles  # Получаем список всех открытых вкладок
        new_tab_handle = windows_handles[-1]
        driver.switch_to.window(new_tab_handle)  # Переключение на новую вкладку
        time.sleep(10)   # Исключаем появление запроса "Вы робот?"

    with allure.step("Проверка наличия товаров в поиске"):
        find_elements = driver.find_element(
            By.CSS_SELECTOR, '[data-testid="search-results-title"]')
        text_search = find_elements.text.split(" ")

        assert int(text_search[1]) > 0

    with allure.step("Добавляем товар в корзину"):
        card_page.add_product()

    with (allure.step("Проверка суммы товаров в корзине")):
        checkout = driver.find_element(
            By.CSS_SELECTOR, 'span.Price_root.NewCartPriceButton_price')
        text_checkout = checkout.text.split("\u2009")

        assert int(text_checkout[0]) > 0, (
            f"Фактическая сумма: {int(text_checkout[0])}")


@allure.suite("Тестирование магазина")
@allure.title("Проверка очистки корзины")
@allure.description("Тест проверяет возможность полной очистки корзины.")
@allure.feature("Очистка корзины")
@allure.severity(allure.severity_level.BLOCKER)
def test_clear_cart(driver):
    with allure.step("Загрузка браузера"):
        first_page = FirstPage(driver)
        first_page.go()
        time.sleep(15)

    with allure.step("Вносим адрес доставки"):
        main_page = MainPage(driver)
        address = "Большой Дровяной переулок, 10, Москва\n"
        main_page.add_address(address)
        time.sleep(2)

    with allure.step("Поиск прдуктов"):
        product = "молоко"
        main_page.open_find(product)

    with allure.step("Выбираем товар"):
        card_page = CardPage(driver)
        card_page.store_selection()

    with allure.step("Переход в новую вкладку"):
        windows_handles = driver.window_handles     # Получаем список всех открытых окон (вкладок)
        new_tab_handle = windows_handles[-1]
        driver.switch_to.window(new_tab_handle)     # Переключение на новую вкладку
        time.sleep(3)   # Исключаем появление запроса "Вы робот?"

    with allure.step("Добавляем товар в корзину"):
        card_page.add_product()

    with allure.step("Очищаем корзину"):
        card_page = CardPage(driver)
        card_page.clear_checkout()

    with (allure.step("Проверка пустой корзины")):
        find_cart = driver.find_element(By.CSS_SELECTOR, 'h3')
        text_cart = find_cart.text.strip()
        expected_text = "В вашей корзине \nпока пусто"

        assert text_cart == expected_text, (
            f"Фактическое сообщение: {text_cart}, ожидалось: {expected_text}")
