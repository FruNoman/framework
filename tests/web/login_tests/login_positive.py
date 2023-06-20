import time
import allure
from ui.pages.home_pages.home_page import HomePage
from ui.pages.headers.header_page import HeaderPage

from ui.elements.categories import Categories


@allure.parent_suite('Login suite')
@allure.suite('Positive login')
def test_positive_login(driver):
    driver.get('https://rozetka.com.ua/ua/')
    home_page = HomePage(driver)
    home_page.header.open_account()
    time.sleep(5)
