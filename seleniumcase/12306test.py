import traceback

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(r'F:\PY\chromedriver.exe')
driver.implicitly_wait(10)
try:

    driver.get('https://kyfw.12306.cn/otn/leftTicket/init')
    fromStation = driver.find_element_by_id('fromStationText')
    fromStation.click()
    fromStation.send_keys(u'南京南\n')

    toStation = driver.find_element_by_id('toStationText')
    toStation.click()
    toStation.send_keys(u'杭州东\n')
    Select(driver.find_element_by_id('cc_start_time')).select_by_visible_text('06:00--12:00')
    driver.find_element_by_css_selector('#date_range li：nth-child(2)').click()
    #使用xpath选择器选车次（先找到二等座有票-再往前查找节点车次）
    xpath = "//*[@id='queryLeftTable']//td[3][@class]/../td[1]//a"
    theTrains = driver.find_elements_by_xpath(xpath)
    for one in theTrains:
        print(one.text)
except:
    print(traceback.format_exc())
finally:
    driver.quit()