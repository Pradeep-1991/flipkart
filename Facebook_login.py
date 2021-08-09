from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r"D:\selinium_drivers\chromedriver_win32\chromedriver")
driver.get("https://www.facebook.com/")
time.sleep(2)
driver.find_element_by_id("email").send_keys("8908469816")
time.sleep(2)
driver.find_element_by_id("pass").send_keys("deepakmohanta")
time.sleep(2)
driver.find_element_by_name("login").send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element_by_class_name("tojvnm2t a6sixzi8 abs2jz4q a8s20v7p t1p8iaqh k5wvi7nf q3lfd5jv pk4s997a bipmatt0 cebpdrjk qowsmv63 owwhemhu dp1hu0rb dhp61c6y iyyx5f41").click()
time.sleep(2)
driver.find_element_by_class_name("d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v ekzkrbhg oo9gr5id hzawbc8m").click()
