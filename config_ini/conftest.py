import pytest
from selenium import webdriver
# from read_config import get_config
import read_config

@pytest.fixture()
def setup_and_teardown(request):
    browser=read_config.get_config("basic info", "browser")
    url=read_config.get_config("basic info", "url")
    if browser=="chrome":
        driver=webdriver.Chrome()
    else:
        driver=webdriver.Edge()
    driver.maximize_window()
    driver.get(url)
    request.cls.driver=driver
    yield
    driver.quit()
