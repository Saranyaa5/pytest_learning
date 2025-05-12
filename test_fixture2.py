import time
from selenium.webdriver.common.by import By

def test_google_search_hp(driver):
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("hp")
    search_box.submit()
    time.sleep(3)
    assert "hp" in driver.title.lower()

def test_google_search_invalid(driver):
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("asldkfjalskdfj1234nonexistent")
    search_box.submit()
    time.sleep(3)
    results = driver.find_elements(By.CSS_SELECTOR, "div#search")
    assert len(results) > 0  # Page loads with search results area even for nonsense query

def test_google_search_empty(driver):
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("")
    search_box.submit()
    time.sleep(3)
    # Google typically stays on the same page with suggestions
    assert "Google" in driver.title
