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

# click on hotels
driver.find_element_by_link_text("HOTELS").click()
time.sleep(2)


handles = driver.window_handles
size = len(handles)
print(size)

parent_handle = driver.current_window_handle
driver.switch_to.window(handles[2])
print(driver.title)
driver.switch_to.window(handles[1])
print(driver.title)
driver.switch_to.window(handles[0])
print(driver.title)
#driver.close()


'''
for x in range(size):
  if handles[x] != parent_handle:
    driver.switch_to.window(handles[x])
    print(driver.title)
    driver.find_element_by_id("stationFrom").send_keys("ahmedabad")
    driver.find_element_by_id("stationTo").send_keys("bhubaneswar")
    time.sleep(5)
    #driver.close()
    break
'''
# driver.switch_to.window(parent_handle)
# print(driver.title)

# driver.find_element_by_id("link").click()
# driver.close()
