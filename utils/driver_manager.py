from selenium import webdriver
from configparser import ConfigParser
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService


def firefox_driver(config: ConfigParser):
    service = FirefoxService(executable_path=config['drivers']['gecko_path'])
    options = webdriver.FirefoxOptions()
    options.binary_location = config['browsers']['firefox_binary']
    driver = webdriver.Firefox(options=options, service=service)
    driver.maximize_window()
    driver.implicitly_wait(int(config['waiters']['implicitly_wait']))
    return driver


def chrome_driver(config: ConfigParser):
    service = ChromeService(executable_path=config['drivers']['chrome_path'])
    options = webdriver.ChromeOptions()
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")

    options.add_argument('--remote-debugging-port=9399')
    driver = webdriver.Chrome(options=options, service=service)
    driver.maximize_window()
    driver.implicitly_wait(int(config['waiters']['implicitly_wait']))
    return driver
