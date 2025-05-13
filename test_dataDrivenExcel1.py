import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities import excel_reader


@pytest.mark.parametrize("username,password",excel_reader.get_data("C:\pytest_learning\ExcelFiles\loginData.xlsx","login"))
class TestLogin1:
    def test_validlogin1(self,username,password):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoblaze.com/index.html")
        self.driver.find_element(By.ID,value="login2").click()
        time.sleep(2)
        self.driver.find_element(By.ID,"loginusername").send_keys(username)
        time.sleep(2)
        self.driver.find_element(By.ID,"loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH,"//button[text()='Log in']").click()
        time.sleep(5)
        if username=="admi" and password=="admi":
            alert = self.driver.switch_to.alert
            actual_text = alert.text
            assert actual_text=="Wrong password."
            alert.accept()
            self.driver.find_element(By.XPATH,"//*[@id='logInModal']/div/div/div[1]/button").click()

        else:
            assert self.driver.find_element(By.ID,"logout2").is_displayed()
        self.driver.quit()