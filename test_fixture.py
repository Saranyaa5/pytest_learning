import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
import pytest

@pytest.fixture()
def test_set_up_and_teardown():
    global driver
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    yield
    driver.quit()

def test_hp(test_set_up_and_teardown):
    driver.find_element(By.NAME,value="search").send_keys("hp")
    driver.find_element(By.XPATH,value="//*[@id='search']/span/button").click()
    driver.find_element(By.XPATH,value="//*[@id='content']/div[3]/div/div/div[2]/div[1]/h4/a").click()
    time.sleep(3)
    assert (driver.find_element(By.XPATH,"//*[@id='content']/div/div[2]/h1").text).__eq__("HP LP3065")

def test_invalid(test_set_up_and_teardown):
    driver.find_element(By.NAME,value="search").send_keys("demo")
    driver.find_element(By.XPATH,value="//*[@id='search']/span/button").click()
    time.sleep(3)
    assert (driver.find_element(By.XPATH,"//*[@id='content']/h2").text).__eq__("Products meeting the search criteria")

def test_empty(test_set_up_and_teardown):
    driver.find_element(By.NAME,value="search").send_keys("")
    driver.find_element(By.XPATH,value="//*[@id='search']/span/button").click()
    time.sleep(3)
    assert (driver.find_element(By.XPATH,"//*[@id='content']/p[2]").text).__eq__("There is no product that matches the search criteria.")
    
