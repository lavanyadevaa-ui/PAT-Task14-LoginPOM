import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://v2.zenclass.in/login")
    yield driver
    driver.quit()

def test_successful_login(driver):
    login = LoginPage(driver)
    login.enter_email("lavanyadevaa@gmail.com")
    login.enter_password("Hasmith@123003")
    login.click_login()
    # Assert on actual page content
    assert "GUVI" in driver.title


def test_unsuccessful_login(driver):
    login = LoginPage(driver)
    login.enter_email("wrong@example.com")
    login.enter_password("wrongpassword")
    login.click_login()
    msg = login.get_invalid_user_message()
    assert "*Invalid email!" in msg


def test_validate_input_boxes(driver):
    login = LoginPage(driver)
    assert driver.find_element(*LoginPage.email_input).is_displayed()
    assert driver.find_element(*LoginPage.password_input).is_displayed()

def test_logout_functionality(driver):
    login = LoginPage(driver)
    login.enter_email("lavanyadevaa@gmail.com")
    login.enter_password("Hasmith@123003")
    login.click_login()

    # Step 1: Close the ad popup
    login.close_ad()

    # Step 2: Wait for profile icon and click
    login.wait.until(EC.presence_of_element_located(LoginPage.profile_icon))
    login.click_profile_icon()

    # Step 3: Wait for logout option and click
    login.wait.until(EC.presence_of_element_located(LoginPage.logout_button))
    login.click_logout()

    # Step 4: Wait for login button to reappear
    login.wait.until(EC.presence_of_element_located(LoginPage.login_button))
    assert driver.find_element(*LoginPage.login_button).is_displayed()
