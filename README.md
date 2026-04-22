Tensor selenium autotest - проект для функционального автотестирования, выполненного по методу черного ящика и призванного проверить работоспособность пользовательского интерфейса сайтов tensor.ru, saby.ru.

## Технологический стек
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org)
[![Pytest](https://img.shields.io/badge/pytest-0A9DD9?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/en/stable/)
[![Selenium](https://img.shields.io/badge/selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/)

## Установка
1. Клонируйте репозиторий на компьютер
    ```
    git clone https://github.com/AlekseyGusev157/tensor_selenium_autotest.git

    ```
## Локальное развертывание проекта
1. Создайте и активируйте виртуальное окружение:
    ```
    cd Tensor_selenium_test

    python3 -m venv env
    ```    
    Если у вас Linux/macOS
    ```
    source env/bin/activate
    ```
    Если у вас windows
    ```
    source env/scripts/activate
    ```
2. Установите зависимости из файла requirements.txt:
    ```
    pip install -r requirements.txt
    ```
3. Запустите проект:
    ```
    pytest
    ```
    Для запуска определенного теста из корневой директории проекта
    ```
    pytest tests/test_tensor.py::TestSaby::test_name
    ```

## Автор
* [**Алексей Гусев**](https://github.com/AlekseyGusev157) 
* Контакты: Ankalagon157@yandex.ru; (https://t.me/AlekseyAnoushirvan)