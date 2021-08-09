import unittest
import HtmlTestRunner
from selenium.webdriver.common.keys import Keys
from unittest.suite import TestSuite
from unittest.case import expectedFailure
import time
from selenium import webdriver

class flipkart_order_placing(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(r"D:\selinium_drivers\chromedriver_win32\chromedriver")
        print ("browser opened")

    def tearDown(self):
        self.driver.quit()
        print("browser closed")


    def test_flipkart(self):
        #open flipkart
        self.driver.get("https://www.flipkart.com/")
        print("Flipkart page opened")

        #user login

        self.driver.find_element_by_xpath("//body/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/input[1]").send_keys("pradeep.mohanta174@gmail.com")
        self.driver.find_element_by_xpath("//body/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/input[1]").send_keys("pradeep.pk")
        time.sleep(5)
        self.driver.find_element_by_xpath("//body/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/button[1]").click()
        time.sleep(5)

        #search product
        self.driver.find_element_by_name("q").send_keys("mobile phone")
        time.sleep(3)
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER)
        time.sleep(15)
        self.driver.find_element_by_xpath("//div[contains(text(),'realme C20 (Cool Blue, 32 GB)')]").click()
        time.sleep(3)
        print(self.driver.title)

        #switching product detail window
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(25)
        print(self.driver.title)

        #add to Cart
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//button[contains(@class,'_2KpZ6l _2U9uOA _3v1-ww')]").click()

        #place order
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[contains(@class,'_2KpZ6l _2ObVJD _3AWRsL')]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(),'Deliver Here')]").click()
        self.driver.find_element_by_xpath("//*[contains(text(),'CONTINUE')]").click()


if __name__ == "__main__":
    #unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:\pythonProject\SeleniumTest\practice\Test_Reports"))

