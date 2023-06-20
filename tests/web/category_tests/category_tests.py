import time
import allure
from ui.pages.home_pages.home_page import HomePage
from ui.elements.categories import Categories


@allure.parent_suite('Category suite')
@allure.suite('Positive login')
def test_category_check(driver):
    driver.get('https://rozetka.com.ua/ua/')
    home_page = HomePage(driver)
    home_page.select_category(Categories.PRODUCTS_FOR_GAMERS)
    time.sleep(5)
