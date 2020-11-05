from selenium import webdriver
driver = webdriver.Chrome(r'F:\PY\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://www.51job.com')
driver.find_element_by_css_selector('a[href*=advance]').click()
driver.find_element_by_id('kwdselectid').send_keys('Python')
driver.find_element_by_id('work_position_input').click()
import time
time.sleep(5)
selectcitys = driver.find_elements_by_css_selector(
    '#work_position_click_center_right_list_000000 em[class=on]')
time.sleep(5)
for one in selectcitys:
    time.sleep(5)
    one.click()
driver.find_element_by_css_selector('em[data-value="080200"]').click()
driver.find_element_by_id('work_position_click_bottom_save').click()
#选职能类别
driver.find_element_by_css_selector('div.tit>span').click()
driver.find_element_by_id('funtype_click').click()
driver.find_element_by_id('funtype_click_center_right_list_category_0100_2700').click()
driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_2707').click()
driver.find_element_by_id('funtype_click_bottom_save').click()
#选择公司类别
driver.find_element_by_id('cottype_list').click()
driver.find_element_by_css_selector('#cottype_list span[data-value="01"]').click()
#选择工作年限
driver.find_element_by_id('workyear_list').click()
driver.find_element_by_css_selector('#workyear_list span[data-value="02"]').click()
driver.find_element_by_css_selector('span[onclick*=kwdselectid]').click()

#筛选工作岗位信息
jobs = driver.find_elements_by_css_selector('#resultList div[class="el"]')
for job in jobs:
    file = job.find_elements_by_tag_name('span')
    strfile = [files.text for files in file]
    print('|'.join(strfile))
print('请输入任意键退出')
driver.quit()









print('输入任意键退出。。。')
driver.quit()