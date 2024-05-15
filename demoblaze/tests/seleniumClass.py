import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MyTests(unittest.TestCase):
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

    def test_case1(self):
        self.driver.get("https://www.demoblaze.com/")
        print(self.driver.title)
        assert "STORE" in self.driver.title
        self.driver.find_element(By.ID, "login2").click()
        username = self.wait.until(EC.element_to_be_clickable((By.ID, "loginusername")))
        username.send_keys("Skillbrain")
        self.driver.find_element(By.ID, "loginpassword").send_keys("password")
        self.driver.find_element(By.CSS_SELECTOR, "button[onclick='logIn()']").click()
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

    def test_case2(self):
        print("hello world")


if __name__ == "__main__":
    unittest.main()
#driver.quit()