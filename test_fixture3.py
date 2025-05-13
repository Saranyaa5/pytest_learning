from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

@pytest.mark.usefixtures("set_up_and_teardown")
class Test_Search:
    def test_google_search_hp(self):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("hp")
        search_box.submit()
        WebDriverWait(self.driver, 10).until(EC.title_contains("hp"))
        assert "hp" in self.driver.title.lower()

    def test_google_search_invalid(self):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("asldkfjalskdfj1234nonexistent")
        search_box.submit()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "search")))
        results_text = self.driver.find_element(By.ID, "search").text
        assert "did not match any documents" not in results_text.lower()

    def test_google_search_empty(self):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("")
        search_box.submit()
        WebDriverWait(self.driver, 10).until(EC.title_contains("Google"))
        assert "Google" in self.driver.title