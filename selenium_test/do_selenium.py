from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#获取cookie信息
cookie = driver.get_cookies()
print(cookie)
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'kw')))#元素的定位类型和表达式
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
# driver.implicitly_wait(30)
#截取页面的当前窗口，并指定页面保存的位置
driver.get_screenshot_as_file("F:\\pythonwork\\selenium_test\\shot_cut\\baidu.png")
time.sleep(1.5)
driver.quit()

# frame的切换方式
driver.switch_to.frame(driver.find_element_by_xpath("")) #切换iframe输入框 ,可以点击frame，查看源码
time.sleep(0.5)
driver.find_element_by_id('')
#切换frame的方式
WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it(''))

#frame切回默认的页面
driver.switch_to.default_content()

