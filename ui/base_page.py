import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    UNIQUE = (By.CSS_SELECTOR, "unique")

    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.__find_uniq_element(self.UNIQUE)

    def __find_uniq_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find {self.__class__.__name__} "
                                                              f"UNIQUE element by locator {locator}")

    def find_element(self, locator, time=10) -> WebElement:
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10) -> WebElement:
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")
