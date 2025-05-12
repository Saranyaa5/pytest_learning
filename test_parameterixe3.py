import pytest
from selenium import webdriver

@pytest.mark.parametrize("drivertype",['chrome'])
@pytest.mark.parametrize("url",['https://www.flipkart.com/','https://www.amazon.in/'])
def test_sample(drivertype,url):
    if drivertype=="chrome":
       driver=webdriver.Chrome()
    elif drivertype=="edge":
        driver=webdriver.Edge()
    driver.maximize_window()
    driver.get(url)
    print(driver.title)