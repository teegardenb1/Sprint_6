from locators.base_page_locators import HeaderLocators, MainPageLocators
from locators.order_page_locators import OrderPageLocators

class Urls:
    start_url = 'https://qa-scooter.praktikum-services.ru/'
    dzen_url = 'https://dzen.ru/?yredirect=true'
    order_url = 'https://qa-scooter.praktikum-services.ru/order'


class TestUsers:
    test_user_1 = {
        'button': HeaderLocators.header_order_button,
        'first_name': 'Анастасия',
        'last_name': 'Лунина',
        'address': 'Улица Панфилова, 16',
        'metro': 'Авиамоторная',
        'telephone': '88005553535',
        'calendar': '10.02.2025',
        'rental': OrderPageLocators.one_day_rental,
        'color': OrderPageLocators.black_color_checkbox,
        'comment': 'Домофон не работает'
    }

    test_user_2 = {
        'button': MainPageLocators.main_order_button,
        'first_name': 'Роман',
        'last_name': 'Васильев',
        'address': 'проезд Завода Серп и Молот, 10',
        'metro': 'Авиамоторная',
        'telephone': '84957602738',
        'calendar': '01.05.2025',
        'rental': OrderPageLocators.five_day_rental,
        'color': OrderPageLocators.grey_color_checkbox,
        'comment': 'К 15:00'
    }

class Questions:
    expected_question_text = [
            'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
            'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
            'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
            'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
            'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
            'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
            'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
            'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
    ]



