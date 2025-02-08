from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Поле ввода "Имя"
    name_field = [By.XPATH, "//input[@placeholder='* Имя']"]
    # Поле ввода "Фамилия"
    last_name_field = (By.XPATH, "//input[@placeholder='* Фамилия']")
    # Поле ввода "Адрес: куда привезти заказ"
    address_field = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    # Выпадающий список станций метро
    dropdown_metro_station = (By.XPATH, "//input[@placeholder='* Станция метро']")
    # Выбор станции метро
    choose_metro = (By.XPATH, ".//div[text() = 'Авиамоторная']")
    # Поле ввода номера телефона
    phone_number_field = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    # Кнопка "Далее"
    next_button = (By.XPATH, "//button[text()='Далее']")
    # Поле ввода "Когда привезти самокат"
    when_to_bring_scooter_field = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    # Выпадающий список "Срок аренды"
    rental_period_place = (By.XPATH, ".//span[@class='Dropdown-arrow']")
    # Выбор срока аренды
    one_day_rental = (By.XPATH, "//div[text()='сутки']")
    two_day_rental = (By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']")
    three_day_rental = (By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']")
    four_day_rental = (By.XPATH, "//div[@class='Dropdown-option' and text()='четверо суток']")
    five_day_rental = (By.XPATH, "//div[@class='Dropdown-option' and text()='пятеро суток']")
    six_day_rental = (By.XPATH, "//div[@class='Dropdown-option' and text()='шестеро суток']")
    seven_day_rental = (By.XPATH, "//div[@class='Dropdown-option' and text()='семеро суток']")
    # Чекбокс цвета "чёрный жемчуг"
    black_color_checkbox = (By.XPATH, "//input[@id='black']")
    # Чекбокс цвета "серая безысходность"
    grey_color_checkbox = (By.XPATH, "//input[@id='grey']")
    # Поле ввода "Комментарий для курьера"
    comment_field = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    # Кнопка "Назад"
    backspace_button = (By.XPATH, "//button[text()='Назад']")
    # Кнопка "Заказать"
    order_button = (By.XPATH, "(//button[contains(@class, 'Button_') and text()='Заказать'])[2]")
    # Кнопка "Нет"
    no_button = (By.XPATH, "//button[text()='Нет']")
    # Кнопка "Да"
    yes_button = (By.XPATH, "//button[text()='Да']")
    # Кнопка "Посмотреть статус"
    show_status_button = (By.XPATH, "//button[text()='Посмотреть статус']")
    # Текст об успешном оформлении заказа
    show_status_text = (By.XPATH, "(//div[contains(@class, 'Order_ModalHeader_') and text()='Заказ оформлен'])")