from selenium import webdriver
import pytest
from utilities.config_reader import get_config

@pytest.fixture()
def setup_and_tear_down(request):
    url=get_config("config info","url")
    browser=get_config("config info","browser")
    if browser=="chrome":
        driver=webdriver.Chrome()
    elif browser=="edge":
        driver=webdriver.Edge()
    driver.get(url)
    request.cls.driver=driver
    yield
    driver.quit()

