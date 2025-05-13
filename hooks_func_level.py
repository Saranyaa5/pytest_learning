from selenium import webdriver

def setup_function(function):
    global driver
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://www.google.co.in")

def teardown_function(function):
    driver.quit()

def test_validation():
    expected_title="Google"
    actual_title=driver.title
    assert expected_title.__eq__(actual_title)