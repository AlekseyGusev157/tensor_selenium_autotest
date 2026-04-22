import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_page import BasePage
from locators import Locators


class SabyMain(BasePage):
    """Класс тестируемой веб-страницы Saby для сценария отправки заявки."""

    def __init__(self, browser):
        super().__init__(browser)

    def open_url(self):
        """Метод перехода на тестируемую веб-страницу."""

        self.browser.get('https://saby.ru/')

    def find_product(self):
        """Метод поиска и клика списка цифровых продуктов."""

        self.find_element(Locators.search_menu, time=3).click()
        self.browser.execute_script(
            'arguments[0].click();',
            self.find_element(Locators.click_ofd, time=3)
        )

    def click_form(self):
        """Метод клика формы заявки."""

        button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(Locators.request_button)
        )
        self.browser.execute_script('arguments[0].click();', button)

    def fill_form(self, name, number, email):
        """Метод заполнения и отправки формы заявки."""

        name_input = self.find_element(Locators.name, time=3)
        for char in name:
            name_input.send_keys(char)
            time.sleep(0.1)

        phone_input = self.find_element(Locators.phone_number, time=3)
        for digit in number:
            phone_input.send_keys(digit)
            time.sleep(0.1)

        email_input = self.find_element(Locators.email, time=3)
        for char in email:
            email_input.send_keys(char)
            time.sleep(0.1)

        self.find_element(Locators.agree_personal_data, time=3).click()
        self.find_element(Locators.send_form, time=3).click()

    def success_send(self):
        """Метод проверки уведомления об успешной отправке формы."""

        return self.find_element(Locators.success_send)
