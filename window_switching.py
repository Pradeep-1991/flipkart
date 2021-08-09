from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r"D:\selinium_drivers\chromedriver_win32\chromedriver")
driver.implicitly_wait(5)

driver.get("https://www.irctc.co.in/nget/train-search")
time.sleep(3)

driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()
print("irctc opened")

# click on Air
driver.find_element_by_link_text("FLIGHTS").click()
time.sleep(2)

driver.find_element_by_link_text("HOTELS").click()
time.sleep(2)

'''
#handles = driver.window_handles
driver.switch_to.window(driver.window_handles[1])
print(driver.title)
#time.sleep(3)
driver.switch_to.window(driver.window_handles[2])
print(driver.title)
'''

print(driver.title)

driver.switch_to.window(driver.window_handles[2])
print(driver.title)