from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r"D:\selinium_drivers\chromedriver_win32\chromedriver")

driver.get("https://www.facebook.com")

#driver.get("https://www.facebook.com/recover/initiate/?ars=facebook_login&amp;privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjI1ODQwODczLCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D")

time.sleep(15)

driver.find_element_by_link_text("Forgotten password?").click()

time.sleep(15)

driver.find_element_by_id("identify_email").send_keys("8908469816")
time.sleep(2)

driver.find_element_by_id("did_submit").click()
time.sleep(2)

driver.find_element_by_name("reset_action").click()
time.sleep(10)

password = input("Enter OTP: ")

driver.find_element_by_id("recovery_code_entry").send_keys(password)
time.sleep(2)

driver.find_element_by_name("reset_action").click()
time.sleep(2)

new_password = input("Enter  new password: ")

driver.find_element_by_id("password_new").send_keys(new_password)
time.sleep(1.5)

driver.find_element_by_id("btn_continue").click()
time.sleep(2)

driver.find_element_by_name("manage-sessions").click()
time.sleep(1)

driver.find_element_by_class_name("n00je7tq arfg74bv qs9ysxi8 k77z8yql i09qtzwb n7fi1qx3 b5wmifdl hzruof5a pmk7jnqg j9ispegn kr520xx4 c5ndavph art1omkt ot9fgl3s rnr61an3").click()




driver.quit()
