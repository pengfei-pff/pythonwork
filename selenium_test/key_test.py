from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
#输入框输入值
driver.find_element_by_id('kw').send_keys("柠檬班")
driver.find_element_by_id('su').click()

WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="10"]/h3')))
ele =driver.find_element_by_xpath('//*[@id="10"]/h3')
#使用js滚动条
driver.execute_script("arguments[0].scrollIntoView(false);",ele)

