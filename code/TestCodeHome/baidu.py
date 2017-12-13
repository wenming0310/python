<<<<<<< HEAD
# coding=utf-8
from selenium import webdriver
import time
'''
driver = webdriver.Firefox()
#driver = webdriver.Ie() #c有问题
#driver = webdriver.Chrome()
#driver = webdriver.Edge()#有问题
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()
time.sleep(5)
driver.quit()
'''
'''
driver = webdriver.Firefox()
driver.get("http://m.mail.10086.cn")
print("设置浏览器宽480、高800显示")

#driver.set_window_size(480,800)
driver.maximize_window()
time.sleep(5)
driver.quit()
'''
driver = webdriver.Firefox()
#访问百度首页
first_url = 'http://www.baidu.com'
print("now access %s" %(first_url))
driver.get(first_url)
time.sleep(1)
#访问新闻页
second_url = 'http://news.baidu.com'
print("now access %s" %(second_url))
driver.get(second_url)
time.sleep(1)
#返回（后退）到百度主页
print("back to %s " %(first_url))
driver.back()
#前进到新闻页
time.sleep(1)
print("forward to %s" %(second_url))
driver.forward()

time.sleep(5)
=======
# coding=utf-8
from selenium import webdriver
import time
'''
driver = webdriver.Firefox()
#driver = webdriver.Ie() #c有问题
#driver = webdriver.Chrome()
#driver = webdriver.Edge()#有问题
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()
time.sleep(5)
driver.quit()
'''
'''
driver = webdriver.Firefox()
driver.get("http://m.mail.10086.cn")
print("设置浏览器宽480、高800显示")

#driver.set_window_size(480,800)
driver.maximize_window()
time.sleep(5)
driver.quit()
'''
driver = webdriver.Firefox()
#访问百度首页
first_url = 'http://www.baidu.com'
print("now access %s" %(first_url))
driver.get(first_url)
time.sleep(1)
#访问新闻页
second_url = 'http://news.baidu.com'
print("now access %s" %(second_url))
driver.get(second_url)
time.sleep(1)
#返回（后退）到百度主页
print("back to %s " %(first_url))
driver.back()
#前进到新闻页
time.sleep(1)
print("forward to %s" %(second_url))
driver.forward()

time.sleep(5)
>>>>>>> 228d57760e22242bd39aba4b7829a3e0c41dd95d
driver.quit()