import os
import pytest
from utils import driver_manager
from configparser import ConfigParser

resources = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(autouse=True, scope='session')
def config():
    config = ConfigParser()
    config.read(f'{resources}/config/config.ini')
    yield config


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="firefox", help="set browser name: firefox, chrome"
    )


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(autouse=False, scope='function')
def driver(config, browser):
    match browser:
        case 'chrome':
            driver = driver_manager.chrome_driver(config)
        case 'firefox':
            driver = driver_manager.firefox_driver(config)
        case _:
            driver = driver_manager.firefox_driver(config)
    yield driver
    driver.quit()
