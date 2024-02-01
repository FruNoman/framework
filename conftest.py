import os
import pytest
from configparser import ConfigParser
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

resources = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(autouse=True, scope='session')
def config():
    config = ConfigParser()
    config.read(f'{resources}/config/config.ini')
    yield config


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="set browser name: firefox, chrome"
    )


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(autouse=False, scope='function')
def driver(config, browser):
    match browser:
        case 'chrome':
            service = ChromeService(executable_path=ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
        case 'firefox':
             service = FirefoxService(executable_path=GeckoDriverManager().install())
             driver = webdriver.Firefox(service=service)
        case _:
            service = FirefoxService(executable_path=GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()

