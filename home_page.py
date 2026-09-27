from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage

class HomePage(BasePage):
    LOGOUT = (By.ID, "logoutBtn")

    def logout(self):
        self.click(self.LOGOUT)

    def is_logged_out(self):
        try:
            return self.driver.find_element(By.ID, "login").is_displayed()
        except NoSuchElementException:
            return False
