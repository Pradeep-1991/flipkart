from selenium import webdriver
import time

driver = webdriver.Chrome((r"D:\selinium_drivers\chromedriver_win32\chromedriver"))


driver.get ("https://www.guru99.com/")

time. sleep(5)

driver.find_element_by_xpath("//body/div[@id='g-page-surround']/section[@id='g-showcase']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]").click()

time.sleep(5)

driver.quit()

