from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(10)
driver.get("https://www.demoblaze.com/")
wait = WebDriverWait(driver, 10)
print(driver.title)
assert "STORE" in driver.title

driver.find_element(By.ID, "login2").click()
username = wait.until(EC.element_to_be_clickable((By.ID, "loginusername")))
username.send_keys("Skillbrain")
driver.find_element(By.ID, "loginpassword").send_keys("password")
driver.find_element(By.CSS_SELECTOR, "button[onclick='logIn()']").click()
alert = wait.until(EC.alert_is_present())
alert.accept()

#driver.quit()