from selenium import  webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.126.com")
'''
driver.find_element_by_id("idInput").clear()
driver.find_element_by_id("idInput").send_keys("username")
driver.find_element_by_id("pwdInput").clear()
driver.find_element_by_id("pwdInput").send_keys("password")
driver.find_element_by_id("loginBtn").click()
'''
'''
#id会变
driver.find_element_by_id("auto-id-1508945689189").clear()
driver.find_element_by_id("auto-id-1508945689189").send_keys("username")
driver.find_element_by_id("auto-id-1508945689190").clear()
driver.find_element_by_id("auto-id-1508945689190").send_keys("password")
driver.find_element_by_id("dologin").click()
'''

driver.find_element_by_css_selector("html body div#cnt-box-parent.g-bd.cnt-box-include div#cnt-box.g-bd div.m-cnt form#login-form div#auto-id-1508946663594.m-container div#account-box.inputbox div#auto-id-1508946663597.u-input.box input#auto-id-1508946663560.j-inputtext.dlemail").clear()
driver.find_element_by_css_selector("html body div#cnt-box-parent.g-bd.cnt-box-include div#cnt-box.g-bd div.m-cnt form#login-form div#auto-id-1508946663594.m-container div#account-box.inputbox div#auto-id-1508946663597.u-input.box input#auto-id-1508946663560.j-inputtext.dlemail").send_keys("username")
driver.find_element_by_css_selector("html body div#cnt-box-parent.g-bd.cnt-box-include div#cnt-box.g-bd div.m-cnt form#login-form div#auto-id-1508945955095.m-container div#auto-id-1508945955097.inputbox div#auto-id-1508945955098.u-input.box").clear()
driver.find_element_by_css_selector("html body div#cnt-box-parent.g-bd.cnt-box-include div#cnt-box.g-bd div.m-cnt form#login-form div#auto-id-1508945955095.m-container div#auto-id-1508945955097.inputbox div#auto-id-1508945955098.u-input.box").send_keys("password")
driver.find_element_by_css_selector("html body div#cnt-box-parent.g-bd.cnt-box-include div#cnt-box.g-bd div.m-cnt form#login-form div#auto-id-1508945955095.m-container div.f-cb.loginbox a#dologin.u-loginbtn.btncolor.tabfocus.btndisabled").click()

time.sleep(5)
driver.quit()