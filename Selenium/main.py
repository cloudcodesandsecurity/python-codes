import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


# This is a Web Scrapper Tool
chrome_driver_path = "C:\gitrepos\cloudcodesandsecurity\pythoncodes\Selenium\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# For XPath
driver.get("https://www.amazon.com/dp/B09F6XHB4C/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0")


for elem in driver.find_elements(By.XPATH, '//*[@id="amazonGlobal_feature_div"]/span[1]'):
    print(elem.text)


# price = driver.find_element(By.CLASS_NAME, "a-offscreen")
# print(price.text)


# driver.close()
driver.quit()



