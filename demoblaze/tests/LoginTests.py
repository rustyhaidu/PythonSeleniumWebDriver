import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from demoblaze.pageobjects.LoginPage import LoginPage


class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_experimental_option("detach", True)
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.wait = WebDriverWait(cls.driver, 10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_negative(self):
        self.driver.get("https://www.demoblaze.com/")
        login_page = LoginPage(self.driver)
        login_page.login("Skillbrain", "password")
        login_page.accept_alert()


if __name__ == "__main__":
    unittest.main()
