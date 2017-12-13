# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
#time.sleep(5)
#driver.
driver.get("https://www.baidu.com")

#time.sleep(3)
driver.fine_element_by_id("ku").send_keys("Selenium2")
driver.find_element_by_id("su").click()
driver.quit()
