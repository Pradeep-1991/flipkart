from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome((r"D:\selinium_drivers\chromedriver_win32\chromedriver"))
action = ActionChains(driver)
driver.get("https://chercher.tech/practice/drag-drop")

from_element = driver.find_element_by_id("box1")
#time.sleep(2)


to_element = driver.find_element_by_id("destination")
#time.sleep(2)

action.drag_and_drop(from_element,to_element)

action.perform()