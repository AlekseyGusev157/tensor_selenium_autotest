from selenium.webdriver.common.by import By


class Locators:
    """Локаторы для поиска элементов на веб-странице."""

    contacts = (By.CSS_SELECTOR, '[href="/contacts"]')
    download = (By.CSS_SELECTOR, '[href="/download"]')
    force_in_people = (
        By.CSS_SELECTOR,
        '.tensor_ru-Index__block4-bg .tensor_ru-Index__card-title'
    )
    force_in_people_about = (
        By.CSS_SELECTOR,
        '.tensor_ru-Index__block4-bg .tensor_ru-Index__card-text a'
    )
    kamchatka_region = (By.XPATH, '//*[contains(text(), "Камчатский край")]')
    new_partner = (
        By.CSS_SELECTOR, '[title="пр-кт Карла Маркса, д. 31/2, оф. 315"]'
    )
    partners_list = (By.CLASS_NAME, 'sbisru-Contacts-List__item')
    plugin = (By.CSS_SELECTOR, 'div.controls-TabButton[data-id="support"]')
    region = (
        By.XPATH,
        "//*[@id='container']/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span"
    )
    tensor = (By.CSS_SELECTOR, '[href="https://tensor.ru/"]')
    windows_download = (
        By.CSS_SELECTOR,
        '[href="https://update.saby.ru/rh/SabyAdminInstaller_win32.exe"]'
    )
    working = (
        By.CSS_SELECTOR,
        '.tensor_ru-About__block3 .tensor_ru-About__block-title'
    )
    working_images = (By.CLASS_NAME, 'tensor_ru-About__block3-image-wrapper')
    # Bonus_locators
    agree_personal_data = (By.CSS_SELECTOR, '[data-qa="controls-CheckboxMarker"]')
    click_ofd = (By.CSS_SELECTOR, '[href="/ofd"]')
    email = (By.CSS_SELECTOR, 'input[placeholder="электронная почта"]')
    name = (By.CSS_SELECTOR, 'input[placeholder="как к вам обращаться"]')
    phone_number = (By.CSS_SELECTOR, 'input[placeholder="номер телефона"]')
    request_button = (By.CSS_SELECTOR, 'button[title="Оставить заявку"]')
    search_menu = (By.CSS_SELECTOR, 'button[aria-label="Кнопка открытия меню"]')
    send_form = (By.CSS_SELECTOR, 'button[title=Отправить]')
    success_send = (By.XPATH, '//*[contains(text(), "Спасибо за заявку")]')
