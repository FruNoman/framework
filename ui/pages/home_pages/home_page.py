import allure
from ui.base_page import BasePage
from ui.pages.headers.header_page import HeaderPage
from selenium.webdriver.common.by import By
from ui.elements.categories import Categories


class HomePage(BasePage):
    UNIQUE = (By.CSS_SELECTOR, ".menu-categories_type_main")
    CATEGORIES = (By.CSS_SELECTOR, ".menu-categories_type_main>li>a")

    @property
    def header(self) -> HeaderPage:
        return HeaderPage(self.driver)

    @allure.step('select category {category}')
    def select_category(self, category: Categories):
        categories_list = self.find_elements(self.CATEGORIES)
        for cat in categories_list:
            if category.value in cat.get_attribute('href'):
                cat.click()
                break
