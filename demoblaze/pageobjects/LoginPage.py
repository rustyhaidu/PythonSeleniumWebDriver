from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.username_locator = (By.ID, "loginusername")
        self.password_locatr = (By.ID, "loginpassword")
        self.login_button_locator = (By.CSS_SELECTOR, "button[onclick='logIn()']")
        self.login_link = (By.ID, "login2")

    def open_login_modal(self):
        login_link = self.driver.find_element(*self.login_link)
        login_link.click()

    def set_username(self, username):
        username_input = self.wait.until(EC.element_to_be_clickable(self.username_locator))
        username_input.clear()
        username_input.send_keys(username)

    def set_password(self, password):
        password_input = self.driver.find_element(*self.password_locatr)
        password_input.clear()
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(*self.login_button_locator)
        login_button.click()

    def login(self, username, password):
        self.open_login_modal()
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()

    def accept_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()