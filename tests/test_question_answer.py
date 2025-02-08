import allure
import pytest
from data import *
from pages.main_page import MainPage


class TestQuestions:

    @allure.title('Тест проверки текста ответов на вопросы на главной странице веб-приложения')
    @pytest.mark.parametrize('questions, answers_text, expected_question_text', zip(MainPageLocators.questions,MainPageLocators.answers_text, Questions.expected_question_text))


    def test_accordion_questions(self, driver, questions, answers_text, expected_question_text):
        main_page = MainPage(driver)
        text = main_page.get_text_question(questions, answers_text)

        assert text == expected_question_text