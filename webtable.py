#
from selenium import webdriver
import time

driver = webdriver.Chrome(r"D:\selinium_drivers\chromedriver_win32\chromedriver")

# Get the website
driver.get("https://www.bseindia.com/sensex/code/16/")

# Make Python sleep for some time
time.sleep(2)

table = driver.find_element_by_xpath("//body/div[@id='skipcontent']/div[@id='fontSize']/div[2]/div[1]/div[2]")
#r = driver.find_elements_by_xpath ("//table[@class= 'spTable']/tbody/tr")
print(table.text)
time.sleep(2)
row = driver.find_element_by_class_name("svboxgreen")
#column = driver.find_element_by_id("mainDiv1")
print(len(row))
#column_count = len(column)