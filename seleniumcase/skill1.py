from selenium import webdriver
import time
driver = webdriver.Chrome(r'F:\PY\chromedriver.exe')
driver.implicitly_wait(10)
driver.get("https://www.baidu.com/")
print(driver.title)
time.sleep(3)
driver.find_element_by_id('kw').send_keys(u'松勤\n')
driver.find_element_by_id(1)
print(driver.title)
driver.get_screenshot_as_file('sq.png')
print(' ')
driver.quit()