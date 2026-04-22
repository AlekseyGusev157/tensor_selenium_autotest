import pytest
from selenium import webdriver


@pytest.fixture()
def web_browser():
    """Функция возвращает браузер для последующего тестирования."""

    edge_browser = webdriver.Edge()
    return edge_browser
