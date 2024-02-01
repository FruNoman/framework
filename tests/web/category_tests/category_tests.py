import time
import allure



@allure.parent_suite('Category suite')
@allure.suite('Positive login')
def test_category_check(driver):
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://de-sprinttest7.dev.lumada.solutions.hitachienergy.com/summary/#appointment-appointment')
    print()


