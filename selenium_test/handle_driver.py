from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
#输入框输入值
driver.find_element_by_id('kw').send_keys("柠檬班")
driver.find_element_by_id('su').click()

WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//a[contains(text(),"吧_百度贴吧")]')))
# handles = driver.window_handles
driver.find_element_by_xpath('//a[contains(text(),"吧_百度贴吧")]').click()
# 等待新窗口的出现
# WebDriverWait(driver,10).until(EC.new_window_is_opened(handles))
time.sleep(0.5) #等待0.5s元素都出现
'''
1、获取窗口的句柄 获取窗口     
'''
handles = driver.window_handles
print(handles)
print(driver.current_window_handle)

driver.switch_to.window(handles[-1])
# button 的id值 j_head_focus_bt
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,'j_head_focus_btn')))

driver.find_element_by_id('j_head_focus_btn').click()



#alert弹框的处理
WebDriverWait(driver,10).until(EC.alert_is_present())
#alert切换 不是html元素
alert =driver.switch_to.alert
#打印alert弹框
print(alert)
#关闭alert弹框
alert.accept()

# 等待+条件