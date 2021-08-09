from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome((r"D:\selinium_drivers\chromedriver_win32\chromedriver"))

driver.get ("https://outlook.live.com/owa/")

#driver.implicitly_wait(0.1)

print("hotmail")

driver.find_element_by_xpath("//a[contains(text(),'Sign in')]").click()
#driver.implicitly_wait(0.1)


driver.find_element_by_id("i0116").send_keys("pradeep.mohanta174@hotmail.com")
#driver.implicitly_wait(0.1)

driver.find_element_by_id("idSIButton9").click()
#driver.implicitly_wait(3)

driver.find_element_by_id("i0118").send_keys("Pradeep.pk")
time.sleep(10)

driver.find_element_by_xpath("//input[contains(@id,'idSIButton9')]").click()
time.sleep(4)

print("login sucessfull")

driver.find_element_by_id("id__7").click()
print("compose new mail")
time.sleep(10)

print("file attachment process starts")

time.sleep(10)
driver.find_element_by_xpath("//span[contains(@id,'id__79')]").click()
time.sleep(10)

#driver.find_element_by_class_name("ms-ContextualMenu-itemText label-244").send_keys("D://python notes//TimeStamps.txt")

driver.find_element_by_xpath("//span[contains(text(),'Browse this computer')]").send_keys("D://python notes//TimeStamps.txt")


