# Финальный проект. Тестирование сервиса Яндекс.Еда "Деливери"

Тесты UI:
Проверяют корректность работы магазинов:
- поиск товара
- добавление товара в корзину
- изменение количества товара в корзине
- проверка суммы товаров
- очистка корзины

Тесты API:
Проверяют корректность заказов блюд из ресторана:
- выбор ресторана
- запрос меню
- выбор блюд


### Шаги
1. Склонировать проект `git clone https://github.com/allatester21/fd.git`
2. Установить все зависимости `pip3 install -r requirements.txt`
3. Запустить тесты `pytest`
4. Сгенерировать отчет 'pytest --alluredir allure-results'
5. Открыть отчет 'allure serve allure-results'

### Стек:
- pytest
- selenium
- webdrawer manager
- requests
- allure
- config
- json

### Струткура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- ./db - хелперы для работы с БД
- test_config.ini - настройки для тестов

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)