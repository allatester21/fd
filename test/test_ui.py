import time
import allure
from selenium.webdriver.common.by import By
from FirstPage import FirstPage
from MainPage import MainPage
from CardPage import CardPage


@allure.suite("Тестирование магазина")
@allure.title("Тестирование покупок в магазине")
@allure.description("Тест проверяет корректность работы магазина: поиск товара, добавление товаров "
                    "в корзину, увеличение товаров в корзине, сумму товаров в корзине "
                    "и очистку корзины.")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    first_page = FirstPage(driver)
    first_page.go()

    time.sleep(20)

    """
    Проверяем, что URL заканчивается на moscow?shippingType=delivery
    """
    assert first_page.get_current_url().endswith("moscow?shippingType=delivery")

    main_page = MainPage(driver)
    address = "Волжский бульвар, 16, корп. 2, Москва\n"
    result_address = main_page.add_address(address)
    time.sleep(2)

    """
    Проверяем, что введенный адрес, отображается вверху страницы
    """
    assert result_address in address

    product = "молоко"
    main_page.open_find(product)

    """
    Проверяем что в списке есть хотя бы один продукт
    """
    find_element = driver.find_element(By.CSS_SELECTOR, 'h1')
    text_array = find_element.text.split(" ")

    assert int(text_array[1]) > 0

    card_page = CardPage(driver)
    card_page.store_selection()

    """
    Переход в открывшуюся вкладку
    """
    windows_handles = driver.window_handles     # Получаем список всех открытых окон (вкладок)
    new_tab_handle = windows_handles[-1]
    driver.switch_to.window(new_tab_handle)     # Переключение на новую вкладку

    time.sleep(5)

    """
    Проверяем, что в списке есть хотя бы один продукт
    """
    find_elements = driver.find_element(By.CSS_SELECTOR, '[data-testid="search-results-title"]')
    text_search = find_elements.text.split(" ")

    assert int(text_search[1]) > 0

    card_page.add_product()

    """
    Проверка, что сумма товаров больше 0 рублей
    """
    checkout = driver.find_element(By.CSS_SELECTOR, 'span.Price_root.NewCartPriceButton_price')
    text_checkout = checkout.text.split("\u2009")

    assert int(text_checkout[0]) > 0

    card_page.clear_checkout()

    """
    Проверяем, что корзина пустая
    """
    find_cart = driver.find_element(By.CSS_SELECTOR, 'h3')
    text_cart = find_cart.text

    assert text_cart == "В вашей корзине \nпока пусто"
