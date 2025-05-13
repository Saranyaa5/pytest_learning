from selenium.webdriver.common.by import By
import pytest
from utilities.excel_reader import get_exceldata
import time

@pytest.mark.usefixtures("setup_and_tear_down")
class TestLogin3:
    login_data = get_exceldata("C:\pytest_learning\saucedemo_practice\excelfile\login_input.xlsx", "Sheet1")

    def test_login_locked_out_user(self):
        username, password = self.login_data[0]
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

        if username == "locked_out_user":
            time.sleep(2)
            assert self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/h3").is_displayed()

    def test_login_standard_user(self):
       
        username, password = self.login_data[1]
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

        if username != "locked_out_user":
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//*[@id='menu_button_container']/div/div[3]/div").click()
            time.sleep(2)
            assert self.driver.find_element(By.XPATH, "//*[@id='logout_sidebar_link']").is_displayed()

    def test_login_problem_user(self):
       
        username, password = self.login_data[2]
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

        if username == "locked_out_user":
            time.sleep(2)
            assert self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/h3").is_displayed()

    def test_login_performance_glitch_user(self):
        
        username, password = self.login_data[3]
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

        if username == "locked_out_user":
            time.sleep(2)
            assert self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/h3").is_displayed()

