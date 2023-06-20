import allure
from ui.base_page import BasePage
from selenium.webdriver.common.by import By


class HeaderPage(BasePage):
    UNIQUE = (By.CSS_SELECTOR, ".header-layout")
    SHOPPING_CART = (By.CSS_SELECTOR, '.header-actions__item--cart')
    ACCOUNT = (By.CSS_SELECTOR, '.header-actions__item--user')

    @allure.step('open shopping cart')
    def open_shopping_cart(self):
        self.find_element(self.SHOPPING_CART).click()

    @allure.step('open account')
    def open_account(self):
        self.find_element(self.ACCOUNT).click()
