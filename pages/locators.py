from selenium.webdriver.common.by import By

class BasePageLocators():
    """Локаторы для базовой страницы"""
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # ссылка на страницу логина
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")  # неверная ссылка для проверки
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")  # иконка пользователя
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")  # ссылка на корзину

class ProductPageLocators():
    """Локаторы для страницы товара"""
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")  # кнопка добавления в корзину
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")  # название товара
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")  # цена товара
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child")  # сообщение об успехе
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")  # общая сумма корзины
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child strong")  # название товара в сообщении

class BasketPageLocators():
    """Локаторы для страницы корзины"""
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")  # товары в корзине
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")  # сообщение о пустой корзине

class LoginPageLocators():
    """Локаторы для страницы логина"""
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")  # форма логина
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")  # форма регистрации
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")  # поле для email
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")  # поле для пароля
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")  # подтверждение пароля
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")  # кнопка регистрации
