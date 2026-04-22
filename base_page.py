from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Базовый класс для выбора браузера и абстрактного поиска элемента."""

    def __init__(self, browser):
        self.browser = browser

    def find_element(self, args, time=10):
        """Метод для поиска элемента."""

        return WebDriverWait(self.browser, time).until(
            EC.visibility_of_element_located(args)
        )

    def find_elements(self, args, time=10):
        """Метод для поиска элементов."""

        return WebDriverWait(self.browser, time).until(
            EC.presence_of_all_elements_located(args)
        )
