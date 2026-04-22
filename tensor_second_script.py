from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_page import BasePage
from locators import Locators


class SabyChangeRegion(BasePage):
    """Класс тестируемой веб-страницы Saby для сценария смены региона."""

    def __init__(self, browser):
        super().__init__(browser)

    def open_url(self):
        """Метод для открытия веб-страницы."""

        self.browser.get('https://saby.ru')

    def click_contacts(self):
        """Метод для перехода в раздел Контакты."""

        self.browser.execute_script(
            'arguments[0].click();',
            self.find_element(Locators.contacts, time=3)
        )

    def find_region(self):
        """Метод для проверки отображения региона."""

        return self.find_element(Locators.region, time=3)

    def find_partners(self):
        """Метод для проверки отображения списка партнеров."""

        return self.find_element(Locators.partners_list, time=3)

    def change_region(self):
        """Метод для смены региона."""

        self.find_region().click()
        self.find_element(Locators.kamchatka_region, time=3).click()

    def check_region_changed(self, expected_region, timeout=5):
        """Метод для подтверждения изменения региона."""

        WebDriverWait(self.browser, timeout).until(
            EC.text_to_be_present_in_element(Locators.region, expected_region)
        )
        return True

    def check_url_contains_region(self, region, timeout=5):
        """Метод для подтверждения изменения региона в url."""

        return WebDriverWait(self.browser, timeout).until(
            EC.url_contains(region.lower())
        )

    def check_title_contains_region(self, region, timeout=5):
        """Метод для подтверждения изменения региона в title."""

        return WebDriverWait(self.browser, timeout).until(
            EC.title_contains(region)
        )

    def check_new_partner(self):
        """Метод для подтверждения изменения партнеров после смены региона."""

        return self.find_element(Locators.new_partner, time=3)
