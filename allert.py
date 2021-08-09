from selenium import webdriver
from selenium.webdriver.common.alert import Alert

from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome((r"D:\selinium_drivers\chromedriver_win32\chromedriver"))

driver.get ("http://demo.automationtesting.in/Alerts.html")
time.sleep(2)

driver.find_element_by_class_name("dropdown-toggle").click()
time.sleep(2)

driver.find_element_by_xpath("//a[contains(text(),'Alerts')]").click()
time.sleep(5)

driver.find_element_by_xpath("//button[contains(text(),'click the button to display an  alert box:')]").click()

#driver.switch_to_alert().accept()

alert=Alert(driver)
alert.accept()
