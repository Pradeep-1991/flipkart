from selenium import webdriver
import time

driver = webdriver.Chrome((r"D:\selinium_drivers\chromedriver_win32\chromedriver"))

driver.get ("https://www.irctc.co.in/nget/train-search")
time.sleep(5)

driver.find_element_by_xpath("//button[contains(@class,'btn btn-primary')]").click()
time.sleep(20)

driver.find_element_by_xpath("//app-header/div[1]/div[2]/a[1]/i[1]").click()
time.sleep(5)

driver.find_element_by_xpath("//button[contains(@class,'search_btn')]").click()
time.sleep(5)

driver.find_element_by_xpath("//input[contains(@id,'userId')]").send_keys("pradip_174")
time.sleep(2)

driver.find_element_by_xpath("//input[contains(@ID,'pwd')]").send_keys("rebati")
time.sleep(2)


#capcha
#driver.find_element_by_xpath("//img[contains(@class,'driver.find_element_by_xpath')]")



driver.quit()



