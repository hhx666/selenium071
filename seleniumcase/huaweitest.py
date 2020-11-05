from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import traceback
driver = webdriver.Chrome(r'F:\PY\chromedriver.exe')
driver.implicitly_wait(30)
try:
    driver.get('https://www.vmall.com/')
    driver.find_element_by_css_selector("div.s-sub a[href*='consumer.huawei']").click()
    driver.find_element_by_css_selector("div.s-sub a.icon-dropdown").click()
    #使用ActionChains方法进行特殊操作
    # ac = ActionChains(driver)
    # ac.move_to_element(driver.find_element_by_css_selector('div.s-sub a.icon-dropdown')).perform()
    driver.find_element_by_css_selector("div a[href*='appstore.huawei']").click()
    #切换到其他网页,跟预期结果作比较
    def Chechuawei():
        excepted = u'''手机|笔记本|平板|智慧屏|穿戴|更多产品|EMUI 10.1|服务支持|零售店|商用'''
        eles = driver.find_elements_by_xpath("//ul[@class='main-nav__list']/li[position()<=10]")
        eletexts = '|'.join(ele.text for ele in eles)
        if eletexts == excepted:
            print('succeful')
        else:
            print('fail')
    def checkappstore():
        expected = u'''推荐|应用|游戏|排行'''
        eles = driver.find_elements_by_css_selector("div.center div")
        elestext = '|'.join(ele.text for ele in eles)
        if elestext == expected:
            print('appsucessful')
        else:
            print('appfail')
    # 使用ActionChains方法进行特殊操作
    def checvmall():
        ecp = '''华为MateBook X系列|华为MateBook系列|华为MateBook D系列|荣耀MagicBook系列|荣耀MagicBook Pro系列'''
        ac = ActionChains(driver)
        ac.move_to_element(driver.find_element_by_css_selector('div.category-info a[href="list-676"]')).perform()
        eles = driver.find_elements_by_css_selector('#zxnav_1 li[class*="subcate-item"]')
        act = '|'.join(ele.text for ele in eles)
        if act == ecp:
            print ('into zhuye')
        else:
            print('fail zhuye')
    mainwindow = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        if u'消费者业务官网' in driver.title:
            Chechuawei()
        elif u'华为应用市场' in driver.title:
            checkappstore()
        # elif u'华为商城' in driver.title:
        #     checvmall()
    driver.switch_to.window(mainwindow)
    checvmall()

except:
    print(traceback.format_exc())
finally:
    driver.quit()
