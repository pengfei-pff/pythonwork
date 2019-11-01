from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
#鼠标操作
#先找到元素
ele = driver.find_element_by_xpath('//*[@id="u1"]/a[8]')
#实例化ActionChains类
ac = ActionChains(driver)
#将鼠标操作添加到action中
ac.move_to_element(ele)
#调用perform（）
ac.perform()

WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//a[text()='高级搜索']")))
driver.find_element_by_xpath("//a[text()='高级搜索']").click()

#select类
from selenium.webdriver.support.ui import Select
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//select[@name='ft']")))
select_ele =driver.find_element_by_xpath("//select[@name='ft']")

#实例化select
s = Select(select_ele)
#方式一：采用下标的方式去选择
s.select_by_index(4)
#方式二：value值
s.select_by_value("all")
#方式三：文本内容
s.select_by_visible_text('Adobe Acrobat PDF (.pdf)')

