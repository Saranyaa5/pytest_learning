import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

# def test_valid_login(setup):
#     driver = setup
#     username = driver.find_element(By.XPATH, "//*[@id='loginPanel']/form/div[1]/input")
#     password = driver.find_element(By.XPATH, "//*[@id='loginPanel']/form/div[2]/input")
#     login = driver.find_element(By.XPATH, "//*[@id='loginPanel']/form/div[3]/input")

#     username.send_keys("Sara1234")
#     password.send_keys("12345")
#     login.click()

#     time.sleep(2)
#     assert driver.title == "ParaBank | Accounts Overview"
#     print("hello saranya")

def test_missing_password(setup):
    driver = setup
    username = driver.find_element(By.XPATH, "//*[@id='loginPanel']/form/div[1]/input")
    login = driver.find_element(By.XPATH, "//*[@id='loginPanel']/form/div[3]/input")

    username.send_keys("sara1234")
    login.click()

    time.sleep(2)
    assert "ParaBank" in driver.title  
