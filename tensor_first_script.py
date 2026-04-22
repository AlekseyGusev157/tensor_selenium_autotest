from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_page import BasePage
from locators import Locators


class SabyContacts(BasePage):
    """Класс тестируемой веб-страницы Saby для сценария перехода на Tensor."""

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

    def find_and_click_tensor(self):
        """Метод для поиска и клика по баннеру Тензор."""

        self.browser.execute_script(
            'arguments[0].click();',
            self.find_element(Locators.tensor, time=3)
        )

    def switch_window(self):
        """Метод для переключения на новую вкладку."""

        self.browser.switch_to.window(WebDriverWait(self.browser, 10).until(
            lambda driver: driver.window_handles[1]
        ))

    def find_force_in_people(self):
        """Метод для поиска раздела 'Сила в людях'."""

        force_in_people = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(Locators.force_in_people)
        )
        self.browser.execute_script(
            "arguments[0].scrollIntoView(true);", force_in_people
        )
        return force_in_people

    def click_force_in_people_about(self):
        """Метод для клика 'Подробнее' в разделе 'Сила в людях'."""

        self.browser.execute_script(
            'arguments[0].click();',
            self.find_element(Locators.force_in_people_about, time=3)
        )

    def check_image_size(self):
        """Метод для проверки равных размеров фото в разделе 'Работаем'."""

        images = self.find_elements(Locators.working_images)

        widths = {image.find_element(By.TAG_NAME, 'img')
                  .get_attribute('width') for image in images}
        heights = {image.find_element(By.TAG_NAME, 'img')
                   .get_attribute('height') for image in images}

        if len(widths) > 1 or len(heights) > 1:
            raise AssertionError('Размеры изображений различаются')
        else:
            return True


