from base_page import BasePage
from locators import Locators


class SabyDownloadPlugin(BasePage):
    """Класс тестируемой веб-страницы Saby для сценария скачивания плагина."""

    def __init__(self, browser):
        super().__init__(browser)

    def open_url(self):
        """Метод для открытия веб-страницы."""

        self.browser.get('https://saby.ru')

    def click_download(self):
        """Метод для перехода в раздел скачивания локальных версий."""

        self.browser.execute_script(
            'arguments[0].click();',
            self.find_element(Locators.download, time=3)
        )

    def find_and_click_plugin(self, timeout=5):
        """Метод для поиска и выбора плагина."""

        self.browser.execute_script(
            'arguments[0].click();',
            self.find_element(Locators.plugin, time=3)
        )

    def download_plugin(self):
        """Метод для скачивания плагина."""

        self.find_element(Locators.windows_download, time=3).click()
