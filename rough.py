from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver =  webdriver.Chrome(r"D:\selinium_drivers\chromedriver_win32\chromedriver")

driver.get("http://admin-demo.nopcommerce.com")
time.sleep(5)

driver.find_element_by_xpath("//button[contains(text(),'Log in')]").click()
time.sleep(5)

driver.find_element_by_xpath("//p[contains(text(),'Customers')]").click()
time.sleep(5)

driver.find_element_by_xpath("//p[contains(text(),' Customers')]").click()
