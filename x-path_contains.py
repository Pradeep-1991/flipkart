from selenium import webdriver
import time

driver = webdriver.Chrome((r"D:\selinium_drivers\chromedriver_win32\chromedriver"))

driver.get ("https://www.guru99.com/")

time. sleep(5)

driver.find_element_by_xpath("//*[contains(@title,'Software Testing')]").click()
time.sleep(5)

driver.quit()

