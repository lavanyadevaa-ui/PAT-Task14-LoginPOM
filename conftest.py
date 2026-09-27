import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://v2.zenclass.in/login")
    driver.maximize_window()
    driver.implicitly_wait(5)  # small implicit wait
    yield driver
    driver.quit()
