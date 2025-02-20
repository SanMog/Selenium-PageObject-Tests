from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math

class BasePage():
    def __init__(self, browser, url, timeout=10):
        """Конструктор класса.
        :param browser: фикстура для работы с браузером
        :param url: адрес страницы
        :param timeout: время ожидания элементов
        """
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """Открывает нужную страницу в браузере"""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """Проверяет наличие элемента на странице
        :param how: как искать (css, id, xpath и тд)
        :param what: что искать (строка-селектор)
        """
        try:
            self.browser.find_element(how, what)
            return True
        except NoSuchElementException:
            return False

    def is_not_element_present(self, how, what, timeout=4):
        """Проверяет, что элемент не появляется на странице в течение заданного времени"""
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
            return False
        except TimeoutException:
            return True

    def is_disappeared(self, how, what, timeout=4):
        """Проверяет, что элемент исчезает со страницы в течение заданного времени"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
            return True
        except TimeoutException:
            return False

    def solve_quiz_and_get_code(self):
        """Решает математическую задачу и получает код для степика"""
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def go_to_basket_page(self):
        """Переходит в корзину по кнопке в шапке сайта"""
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def should_be_authorized_user(self):
        """Проверяет, что пользователь залогинен"""
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented, probably unauthorised user"

    def go_to_login_page(self):
        """Переход на страницу логина"""
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
