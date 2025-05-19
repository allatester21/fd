import rest
import allure


api_url = 'https://market-delivery.yandex.ru'


@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Тестирование заказа блюд")
@allure.title("Поиск ресторана")
@allure.step("Поиск ресторана")
def test_find_rest_positive():
    """
    Ищем ресторан по заданному названию
    """
    rest_name = "foodband"
    cafe, response = rest.test_find_rest(api_url, rest_name)

    assert response.status_code == 200
    assert "FoodBand" in cafe


@allure.suite("Тестирование заказа блюд")
@allure.title("Запрос меню ресторана")
@allure.step("Запрос меню ресторана")
def test_get_menu_positive():
    """
    Запрашиваем меню ресторана
    """
    slug = "foodband_xfuie"
    menu, response = rest.get_menu(api_url, slug)

    assert response.status_code == 200
    assert len(menu) > 0


@allure.suite("Тестирование заказа блюд")
@allure.title("Добавление блюда в корзину")
@allure.step("Добавление блюда в корзину")
def test_add_dish_positive():
    """
    Делаем заказ выбранной позиции
    """
    item_id = 1971750695
    checkaut, id_basket, id_prod, response = rest.add_dish(api_url, item_id)

    assert response.status_code == 200
    assert checkaut > 0
    assert id_basket is not None


@allure.suite("Тестирование заказа блюд")
@allure.title("Запрос меню без указания ресторана")
@allure.step("Запрос меню без указания ресторана")
def test_get_menu_negative():
    """
    Запрашиваем меню, без указания названия ресторана в запросе
    Негативная проверка
    """
    slug = ""
    menu, response = rest.get_menu(api_url, slug)

    assert response.status_code == 200
    assert len(menu) == 0


@allure.suite("Тестирование заказа блюд")
@allure.title("Добавление несуществующего блюда в корзину")
@allure.step("Добавление несуществующего блюда в корзину")
def test_add_dish_negative():
    """
    Делаем заказ позиции, несуществующей в меню
    Негативная проверка
    """
    item_id = 1971750
    checkaut, id_basket, id_prod, response = rest.add_dish(api_url, item_id)
    resp_error = response.json()["errors"]["item_id"][0]

    assert response.status_code == 400
    assert resp_error == (f"menu item {item_id}  не существует")
