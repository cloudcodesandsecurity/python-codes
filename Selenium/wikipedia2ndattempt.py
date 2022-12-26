import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# This is a Web Scrapper Tool
chrome_driver_path = "C:\gitrepos\cloudcodesandsecurity\pythoncodes\Selenium\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# For website scrapping
driver.get("https://sso.teachable.com/secure/teachable_accounts/sign_up")


full_name = driver.find_elements(By.NAME, "teachable_account[name]")
driver.switch_to.active_element.send_keys("Ola-Gabriel")

email = driver.find_elements(By.NAME, "teachable_account[email]")
driver.switch_to.active_element.send_keys("josephola@gmail.com")

password = driver.find_elements(By.NAME, "teachable_account[password]")
driver.switch_to.active_element.send_keys("123456")

confirm_password = driver.find_elements(By.NAME, "teachable_account[password_confirmation]")
driver.switch_to.active_element.send_keys("123456")

term_of_use = driver.find_elements(By.NAME, "teachable_account[agreed_to_terms]")
driver.switch_to.active_element.send_keys(".")

summit = driver.find_elements(By.CSS_SELECTOR, "signup-button button p-v-2-xs p-h-5-xs")
driver.switch_to.active_element.click()







