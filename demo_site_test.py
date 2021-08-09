from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome((r"D:\selinium_drivers\chromedriver_win32\chromedriver"))

driver.get ("http://demo.automationtesting.in/Alerts.html")
time.sleep(2)

driver.find_element_by_link_text("Register").click()
time.sleep(3)

driver.find_element_by_xpath("//input[contains(@placeholder,'First Name')]").send_keys("pradeep")
time.sleep(3)

driver.find_element_by_xpath("//input[contains(@placeholder,'Last Name')]").send_keys("mohanta")
time.sleep(3)

driver.find_element_by_xpath("//textarea[contains(@ng-model,'Adress')]").send_keys("ahmedabad")
time.sleep(3)

driver.find_element_by_xpath("//input[contains(@type,'email')]").send_keys("pradeep@gmail.com")
time.sleep(3)

driver.find_element_by_xpath("//input[contains(@ng-model,'Phone')]").send_keys("0123456789")
time.sleep(1)

driver.find_element_by_xpath("//input[contains(@value,'Male')]").click()
time.sleep(5)

driver.find_element_by_id("checkbox1").click()
driver.find_element_by_id("checkbox2").click()
time.sleep(3)
#sel_lan = Select(driver.find_element_by_id("msdd"))
driver.find_element_by_id("msdd").click()
driver.find_element_by_xpath("//a[contains(text(),'Hindi')]").click()
time.sleep(2)

sel = Select(driver.find_element_by_id("Skills"))
sel.select_by_visible_text('Python')
time.sleep(2)

sel_con = Select(driver.find_element_by_id("countries"))
sel_con.select_by_value("India")
time.sleep(3)

sel_country = Select(driver.find_element_by_id("country"))
sel_country.select_by_visible_text("India")

sel_year =  Select(driver.find_element_by_id("yearbox"))
sel_year.select_by_visible_text("1991")
time.sleep(4)

sel_month = Select(driver.find_element_by_xpath("//body/section[@id='section']/div[1]/div[1]/div[2]/form[1]/div[11]/div[2]/select[1]"))
sel_month.select_by_visible_text("January")

sel_day = Select(driver.find_element_by_id("daybox"))
sel_day.select_by_visible_text("6")

driver.find_element_by_id("firstpassword").send_keys("pradeep")
time.sleep(2)

driver.find_element_by_id("secondpassword").send_keys("prardeep")
time.sleep(3)

driver.find_element_by_id("imagesrc").send_keys("D://2744209.jpg")

driver.find_element_by_id("submitbtn").click()

time.sleep(5)
driver.close()

