import pytest
from pages.product_page import ProductPage
import time
from pages.basket_page import BasketPage

@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:
    """Тесты для авторизованного пользователя"""
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """Предварительная подготовка: открытие страницы товара"""
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        
    def test_user_can_add_product_to_basket(self, browser):
        """Проверяем что авторизованный пользователь может добавить товар в корзину"""
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_success_message()
        page.should_be_correct_price()

    def test_user_cant_see_success_message(self, browser):
        """Проверяем отсутствие сообщения об успехе при открытии страницы товара"""
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    """Проверяем что гость может добавить товар в корзину"""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()
    page.should_be_correct_price()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Проверяем отсутствие сообщения об успехе после добавления товара в корзину"""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """Проверяем что сообщение об успехе исчезает после добавления товара в корзину"""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_disappear_success_message()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """Проверяем что корзина пуста при переходе со страницы товара"""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """Проверяем что гость может перейти на страницу логина со страницы товара"""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
