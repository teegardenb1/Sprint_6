from selenium import webdriver
import pytest
import allure
from data import Urls

@allure.step('Открытие браузера / переход на страницу сервиса / закрытие браузера')
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.start_url)
    driver.maximize_window()
    yield driver
    driver.quit()