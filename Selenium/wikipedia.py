import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# This is a Web Scrapper Tool
chrome_driver_path = "C:\gitrepos\cloudcodesandsecurity\pythoncodes\Selenium\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# For website scrapping
driver.get("https://en.wikipedia.org/wiki/Main_Page")


# https://en.wikipedia.org/wiki/Main_Page
# https://selenium-python.readthedocs.io/
article1 = driver.find_elements(By.LINK_TEXT, ("6,588,852"));
# article1.click()

search = driver.find_elements(By.NAME, "search")
search.send_keys("Python")
search.send_keys(keys.ENTER)


print(article1)


# <a href="/wiki/Special:Statistics" title="Special:Statistics">6,588,764</a>