import pytest
import time
from selenium.webdriver.common.by import By
import read_config

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_validlogin(self):
        self.driver.find_element(By.ID, "login2").click()
        time.sleep(2)
        username = read_config.get_config("login credentials","username")
        password = read_config.get_config("login credentials","pass")
        self.driver.find_element(By.ID,"loginusername").send_keys(username)
        self.driver.find_element(By.ID,"loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH,"//button[text()='Log in']").click()
        time.sleep(5)
        assert self.driver.find_element(By.ID,"logout2").is_displayed()
