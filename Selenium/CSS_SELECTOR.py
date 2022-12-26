import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


# This is a Web Scrapper Tool

chrome_driver_path = "C:\gitrepos\cloudcodesandsecurity\pythoncodes\Selenium\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


# For By.CSS_SELECTOR
driver.get("https://www.python.org/about/")


# https://www.python.org/about/
elem1 = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# print(elem1.text)

elem2 = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# print(elem2.text)

events = {}

for n in range(len(elem1)):
    events[n] = {
        "time": elem1[n].text,
        "name": elem2[n].text,
    }
print(events)


# driver.close()
driver.quit()



