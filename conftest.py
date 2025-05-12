import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.co.in/")
    yield driver
    driver.quit()
