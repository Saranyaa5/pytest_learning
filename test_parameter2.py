import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize('search_item', ['selenium', 'pytest', 'selenium locators'])
def test_google_search(search_item):
    options = Options()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.google.co.in")

    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    search_box.send_keys(search_item)
    search_box.send_keys(Keys.RETURN)

    wait.until(EC.presence_of_element_located((By.ID, "search")))
    assert search_item.lower() in driver.title.lower()
    print(f"Search for '{search_item}' completed. Page title: {driver.title}")
    driver.quit()
