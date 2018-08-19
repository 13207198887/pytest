from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

USER_AGENTS = [
    ' Mozilla/5.0 (Linux; Android 5.1; m1 metal Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 V1ANDSQ7.2.5744YYBD QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080'
]
browser = webdriver.Chrome()
'''百度'''
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#     print(browser.current_url)
# finally:
#     browser.close()

'''淘宝'''
# try:
#     browser.get('https://www.taobao.com')
#     input = browser.find_element_by_id('q')
#     input.send_keys('iphone')
#     time.sleep(1)
#     input.clear()
#     input.send_keys('Ipad')
#     button = browser.find_element_by_class_name('btn-search')
#     button.click()
# finally:
#     browser.close()
# try:
#     browser.get('https://www.taobao.com')
#     href = browser.find_element_by_css_selector('div.site-nav-sign > a:nth-of-type(1)')
#     href.click()
#     choose_up_login = browser.find_element_by_class_name('J_Quick2Static')
#     choose_up_login.click()
#     username = browser.find_element_by_id('TPL_username_1')
#     password = browser.find_element_by_id('TPL_password_1')
#     username.send_keys('18888106880')
#     password.send_keys('7777777su')
#     # 拖动滑块
#     source = browser.find_element_by_id('nc_1_n1z')
#     actions = ActionChains(browser)
#     actions.drag_and_drop_by_offset(source, 258, 0).perform()
#     time.sleep(5)
#     button = browser.find_element_by_id(By.ID, 'J_SubmitStatic')
#     button.click()
# except Exception as e:
#     print(e)
# try:
#     browser.implicitly_wait(10)
#     browser.get('https://www.mayi.com/room/853141513')
#     print(browser.title)
# except Exception as e:
#     print(e)



