import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chromedriver = '/Users/alikhantuxubayev/Documents/environments/chromedriver'

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="ru", help="Choose language: ru, en, es, fr,..")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(chromedriver, options=options)
    browser.check = language
    yield browser
    print("\nquit browser..")
    browser.quit()

