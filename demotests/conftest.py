import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.support.ui import Select


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome') #headless mode starts tests without UI
    options.add_argument('--start-minimized')
    options.add_argument('windows-size=1920x1080')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(executable_path='/chromedriver/chromedriver.exe', options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://demoqa.com/automation-practice-form'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    driver.execute_script("document.body.style.zoom='67%'")
    yield driver
    driver.close()   # закрывает вкладку
    driver.quit()   # закрывает браузер

    