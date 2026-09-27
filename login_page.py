from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Locators
    email_input = (By.XPATH, "//input[@placeholder='Enter your mail']")
    password_input = (By.XPATH, "//input[@type='password']")
    login_button = (By.XPATH, "//button[normalize-space()='Sign in']")
    ad_close_button = (By.XPATH, "/html/body/div[2]/div[3]/div/div/button")
    profile_icon = (By.XPATH, "//img[@id='profile-click-icon']")
    logout_button = (By.XPATH, "//div[normalize-space()='Log out']")
    invalid_user_error = (By.XPATH, "//p[@id=':r1:-helper-text']")

    # Actions
    def enter_email(self, email):
        self.wait.until(EC.presence_of_element_located(self.email_input)).send_keys(email)

    def enter_password(self, password):
        self.wait.until(EC.presence_of_element_located(self.password_input)).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def close_ad(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.ad_close_button)).click()
        except:
            print("No ad popup appeared")

    def click_profile_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.profile_icon)).click()

    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable(self.logout_button)).click()

    def get_invalid_user_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.invalid_user_error)).text
