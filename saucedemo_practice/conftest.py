from selenium import webdriver
import pytest
from utilities.config_reader import get_config
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions

@pytest.fixture()
def setup_and_tear_down(request):
    url = get_config("config info", "url")
    browser = get_config("config info", "browser")
    if browser == "chrome":
        # Set up Chrome options for incognito mode
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == "edge":
        # Set up Edge options for incognito mode
        edge_options = EdgeOptions()
        edge_options.add_argument("--inprivate")
        driver = webdriver.Edge(options=edge_options)
    driver.maximize_window()
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()
