import allure
from data import Urls
from pages.base_page import DzenPage
from pages.main_page import BasePageHeader


class TestHeaderButton:

    @allure.title('Проверка если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»')
    def test_correct_go_to_scooter_button(self, driver):
        base_page = BasePageHeader(driver)
        base_page.first_order_button_click()
        base_page.scooter_logo_click()
        current_url = base_page.get_url()
        title_is_displayed = base_page.check_order_title()
        assert current_url == Urls.start_url and title_is_displayed





    @allure.title('Проверка если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена')
    def test_click_yandex_go_to_dzen(self, driver):
        base_page = BasePageHeader(driver)
        dzen_page = DzenPage(driver)
        current_url = Urls.dzen_url
        base_page.yandex_button_click()
        base_page.go_to_new_tab(Urls.dzen_url)
        assert current_url == Urls.dzen_url and dzen_page.check_element_main_button()