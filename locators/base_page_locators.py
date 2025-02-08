from selenium.webdriver.common.by import By

class HeaderLocators:
    # Логотип "Яндекс"
    yandex_logo = (By.CSS_SELECTOR, "[class*='Header_LogoYandex']")
    # Логотип "Самокат"
    scooter_logo = (By.CSS_SELECTOR, "[class*='Header_LogoScooter']")
    # Кнопка "Заказать" в шапке страницы
    header_order_button = (By.XPATH, "(//button[contains(@class, 'Button_') and text()='Заказать'])[1]")
    # Кнопка "Посмотреть статус"
    status_button = (By.CSS_SELECTOR, "[class*='Header_Link_']")
    # Учебный тренажер
    header_page_title = (By.XPATH, ".//div[text() = 'Учебный тренажер']")


class DzenPageLocators:
    main_button_dzen = (By.XPATH, ".//span[text() = 'Главная']")


class MainPageLocators:
    # Кнопка "Заказать" внизу страницы
    main_order_button = (By.XPATH, "(//button[contains(@class, 'Button_') and text()='Заказать'])[2]")
    # Кнопка "Да все привыкли"
    cooke_button = (By.ID, 'rcc-confirm-button')
    # Форма вопросы о важном
    questions_title = (By.XPATH, "//div[text() = 'Вопросы о важном']")

    # Вопросы о важном
    questions = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7")
    ]
    # Ответы на вопросы о важном
    answers_text = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7")
    ]