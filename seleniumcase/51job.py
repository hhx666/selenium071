#导入webdriver类
from selenium import webdriver
import time
#启动Chrome浏览器
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r'F:\PY\chromedriver.exe')
#30S刷新一次
driver.implicitly_wait(10)
#打开要测试的链接
driver.get('https://www.51job.com')
#搜索框输入Python
driver.find_element_by_id('kwdselectid').send_keys('Python')
#点击搜索城市选择杭州，将所有class为on的城市取消后勾选杭州
driver.find_element_by_id('work_position_input').click()
eles = driver.find_elements_by_css_selector(
    "#work_position_click_center_right_list_000000 em[class=on]")
time.sleep(5)
for one in eles:
    time.sleep(3)
    one.click()
driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click()
#选择杭州后保存
driver.find_element_by_id('work_position_click_bottom_save').click()
#回到主界面点击搜索获取职位信息
driver.find_element_by_css_selector('.ush button').click()
#获取界面搜索到的职位信息
jobs = driver.find_elements_by_css_selector("#resultList div[class='el']")
for job in jobs:
    files = job.find_elements_by_tag_name('span')
    strfile = [file.text for file in files]
    print('|'.join(strfile))
input('输入任意键关闭。。。')
driver.quit()