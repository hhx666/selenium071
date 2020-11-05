#导入webdriver类
from selenium import webdriver
import time
#启动Chrome浏览器
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
#30S刷新一次
driver.implicitly_wait(10)
#打开并登陆快渔
driver.get('http://47.112.110.1:8090/login')
driver.find_element_by_name('username').send_keys('kuaiyu')
driver.find_element_by_name('password').send_keys(123456)
driver.find_element_by_id('btnSubmit').click()
#打印信息管理
# h1 = driver.find_element_by_xpath('//*[@id="side-menu"]/li[3]/a/span[1]')
# print(h1.text)
#进入基础管理
# driver.find_element_by_xpath('//*[@class="fa fa-gear"]').click()
# driver.find_elements_by_css_selector("ul .nav.nav-second-level.collapse.in li:nth-child(1)")[1].click()
#进入首页-客服信息
driver.switch_to.frame("iframe0")
time.sleep(2)
driver.find_element_by_css_selector('h1#addcasecount').click()
# driver.switch_to.default_content()
time.sleep(1)
driver.switch_to.frame('//*[@id="content-main"]/iframe[2]')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="10"]')
driver.find_element_by_css_selector('//*[@id="bootstrap-table"]/tbody/tr[1]/td[6]/a[1]')
# driver.switch_to.default_content()
# driver.find_element_by_css_selector('a.active.menuTab')
# time.sleep(2)
# driver.find_element_by_css_selector('button.dropdown.J_tabClose').click()
# time.sleep(2)
# driver.find_element_by_css_selector("a.tabCloseAll").click()
# 进入首页-订单信息
# driver.switch_to.frame("iframe0")
# driver.find_element_by_css_selector('h1#addcasecount').click()
# time.sleep(2)
# driver.switch_to.default_content()
# time.sleep(1)
# driver.find_elements_by_xpath('/html/body/div/div/div[3]/iframe[2]')
# driver.switch_to.frame(driver.find_elements_by_xpath('/html/body/div/div/div[3]/iframe[2]'))
# driver.find_element_by_css_selector('.box-title')
# driver.find_element_by_css_selector('li.select-time')

# driver.find_element_by_css_selector('a.active.menuTab')
# time.sleep(2)
# driver.find_element_by_css_selector('button.dropdown.J_tabClose').click()
# time.sleep(2)
# driver.find_element_by_css_selector("a.tabCloseAll").click()
# driver.quit()