import allure
import pytest
from data import TestUsers
from pages.main_page import BasePageHeader
from pages.order_page import OrderPage


class TestOrder:

    @allure.title('Проверка позитивного сценария с двумя наборами данных')
    @pytest.mark.parametrize("user_data",[TestUsers.test_user_1, TestUsers.test_user_2])

    def test_correct_oder(self, driver, user_data):
        base_page = BasePageHeader(driver)
        order_page = OrderPage(driver)
        base_page.first_order_button_click()
        order_page.send_first_name(user_data)
        order_page.send_last_name(user_data)
        order_page.send_address(user_data)
        order_page.send_metro(user_data)
        order_page.send_telephone(user_data)
        order_page.click_next_button()
        order_page.send_date(user_data)
        order_page.send_rental_period(user_data)
        order_page.send_color_scooter(user_data)
        order_page.send_comment(user_data)
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.show_status_text()