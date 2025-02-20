from .base_page import BasePage

class MainPage(BasePage):
    """Класс главной страницы магазина"""
    def __init__(self, *args, **kwargs):
        """Конструктор класса"""
        super(MainPage, self).__init__(*args, **kwargs)
