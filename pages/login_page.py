from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        """Проверка страницы логина"""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверка корректности url страницы логина"""
        assert "login" in self.browser.current_url, "Login URL is not correct"

    def should_be_login_form(self):
        """Проверка наличия формы логина"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        """Проверка наличия формы регистрации"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        """Регистрация нового пользователя
        :param email: email пользователя
        :param password: пароль пользователя
        """
        # Заполняем форму регистрации
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_input.send_keys(password)
        confirm_password = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        confirm_password.send_keys(password)
        # Нажимаем кнопку регистрации
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click() 