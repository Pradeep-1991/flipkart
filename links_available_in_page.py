from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(r'D:\selinium_drivers\chromedriver_win32\chromedriver')

driver.get("https://www.google.co.in/")
time.sleep(2)

linkss = driver.find_elements_by_tag_name("a")

#find element using By class
links = driver.find_elements(By.TAG_NAME,"a")
print (len(links))
for link in links:

    print(link.text,"  " , link.get_attribute("href"))


time.sleep(5)
driver.quit()
