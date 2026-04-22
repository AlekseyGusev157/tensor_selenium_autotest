import os

from tensor_bonus import SabyMain
from tensor_first_script import SabyContacts
from tensor_second_script import SabyChangeRegion
from tensor_third_script import SabyDownloadPlugin


class TestSaby:
    """Класс для тестирования различных сценариев на сайтах Saby и Tensor."""

    def test_check_images(self, web_browser):
        """Тестирование первого сценария (переход на Тензор)."""

        saby_to_tensor = SabyContacts(web_browser)
        saby_to_tensor.open_url()
        saby_to_tensor.click_contacts()
        saby_to_tensor.find_and_click_tensor()
        saby_to_tensor.switch_window()
        assert saby_to_tensor.find_force_in_people().is_displayed()
        saby_to_tensor.click_force_in_people_about()
        assert saby_to_tensor.check_image_size() is True

    def test_change_region(self, web_browser):
        """Тестирование второго сценария (смена региона)."""

        saby_regions = SabyChangeRegion(web_browser)
        saby_regions.open_url()
        saby_regions.click_contacts()
        assert saby_regions.find_region().is_displayed()
        assert saby_regions.find_partners().is_displayed()
        saby_regions.change_region()
        assert saby_regions.check_region_changed('Камчатский край')
        assert saby_regions.check_url_contains_region('41-kamchatskij-kraj')
        assert saby_regions.check_title_contains_region('Камчатский край')
        assert saby_regions.check_new_partner().is_displayed()

    def test_download_plugin(self, web_browser):
        """Тестирование третьего сценария (скачивание плагина)."""

        saby_plugin = SabyDownloadPlugin(web_browser)
        saby_plugin.open_url()
        saby_plugin.click_download()
        saby_plugin.find_and_click_plugin()
        saby_plugin.download_plugin()
        file_name = 'SabyAdminInstaller_win32.exe'
        uploaded_file = os.path.join(
            os.path.expanduser('~/Downloads'), file_name
        )
        while True:
            if os.path.exists(uploaded_file) and not (
                uploaded_file.endswith('.crdownload')
            ):
                break
        assert os.path.exists(uploaded_file)
        actual_size_mb = round(
            os.path.getsize(uploaded_file) / (1024 * 1024), 2
        )
        assert actual_size_mb == 20.82

    def test_send_request(self, web_browser):
        """Тестирование бонусного сценария (заполнение и отправка заявки)."""

        saby = SabyMain(web_browser)
        saby.open_url()
        saby.find_product()
        saby.click_form()
        saby.fill_form('name', '9221234567', 'some_mail@ya.ru')
        assert saby.success_send().is_displayed()
