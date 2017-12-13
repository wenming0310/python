from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Firefox()
driver.get("http://yunpan.360.cn")

#right_click = driver.find_element_by_id("#quc_account_376824347")
right_click = driver.find_element_by_css_selector("html body div.index-stage div.login-cont div.login-wrap div.login-box div#login.quc-wrapper.quc-page div.quc-mod-sign-in.quc-mod-normal-sign-in div.quc-main form.quc-form p.quc-field.quc-field-keep-alive a.quc-link.quc-link-about.quc-link-about-normal")
above = driver.find_element_by_css_selector(".icon-windows")
double_click = driver.find_element_by_css_selector("#topPanel > div > div.yp-logo > a")
#鼠标悬停
ActionChains(driver).move_to_element(above).perform()
time.sleep(2)
#鼠标右键单击
ActionChains(driver).context_click(right_click).perform()
time.sleep(2)
#鼠标左键双击
ActionChains(driver).double_click(double_click).perform()
time.sleep(2)
#鼠标拖放
element = driver.find_element_by_css_selector("span.version-item:nth-child(1) > a:nth-child(1) > span:nth-child(2)")
target = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div/div[1]/form/p[1]/span/input")
ActionChains(driver).drag_and_drop(element, target).perform()
time.sleep(2)
driver.quit()