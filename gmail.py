from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r"D:\selinium_drivers\chromedriver_win32\chromedriver")

driver.get("http://demo.guru99.com/test/selenium-xpath.html")
time.sleep(20)

#driver.find_element_by_link_text("Gmail").click()

#for a in driver.find_elements_by_xpath('.//a'):
 #   print(a.get_attribute("href"))

driver.find_element_by_xpath("//input[@name='uid']").send_keys("pradeep")

time.sleep(10)

driver.quit()
