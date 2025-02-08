import allure
from locators.base_page_locators import HeaderLocators, MainPageLocators
from pages.base_page import BasePage


class BasePageHeader(BasePage):

    @allure.step('Клик по логотипу "Яндекс"')
    def yandex_button_click(self):
        self.click_button(HeaderLocators.yandex_logo)

    @allure.step('Клик по логотипу "Самокат"')
    def scooter_logo_click(self):
        self.click_button(HeaderLocators.scooter_logo)

    @allure.step('Клик по кнопке "Заказать" в шапке страницы')
    def first_order_button_click(self):
        self.click_button(HeaderLocators.header_order_button)

    @allure.step('Проверка отображения надписи - "Учебный проект"')
    def check_order_title(self):
        return self.find_and_wait_element(HeaderLocators.header_page_title).is_displayed()


class MainPage(BasePage):

    @allure.step('Скролл и клик по нижней кнопке "Заказать"')
    def second_order_button_click(self):
        self.scroll_to_element(MainPageLocators.main_order_button)
        self.click_button(MainPageLocators.main_order_button)

    @allure.step('Переход к списку вопросов')
    def scroll_to_questions_place(self):
        self.scroll_to_element(MainPageLocators.questions_title)

    @allure.step('Клик на вопрос')
    def click_question_button(self, question_button_locator):
        self.scroll_to_questions_place()
        self.click_button(question_button_locator)

    @allure.step('Получение текста вопроса')
    def get_text_question(self, question_button_locator, question_text_locator):
        self.click_question_button(question_button_locator)
        text_question = self.get_text_locator(question_text_locator)
        return text_question