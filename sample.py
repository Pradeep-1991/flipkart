from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome(r"D:\selinium_drivers\chromedriver_win32\chromedriver")
driver.get("https://www.google.com/")

'''driver.maximize_window()
driver.find_element_by_name("q").send_keys("flipkart")
time.sleep(5)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(5)
'''
action = ActionChains(driver)
action.key_down(Keys.CONTROL).send_keys('f').key_up(Keys.CONTROL)
action.perform()
#driver.find_element_by_name("btnK").click()
