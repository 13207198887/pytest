from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from multiprocessing import Pool
import os
import time

'''
在桌面上必须有个叫qq.txt的文件
格式为:
qq号&密码
qq号&密码

生成cookie.txt也在桌面
'''

mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": ' Mozilla/5.0 (Linux; Android 5.1; m1 metal Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 V1ANDSQ7.2.5744YYBD QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080'
}
chrome_options = Options()
chrome_options.add_argument("--incognito");
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
'''获取qq的cookie'''
src_qq = []
qq_disable = []
path = os.path.join(os.path.expanduser("~"), "Desktop")


def get_cookie(qq):
    try:
        browser = webdriver.Chrome(chrome_options=chrome_options)
        browser.get(
            'https://h5.ele.me/hongbao/#hardware_id=&is_lucky_group=True&lucky_number=5&track_id=&platform=4&sn=29ef424ec3af0418&theme_id=2377&device_id=&refer_user_id=115092954')
        browser.implicitly_wait(10)
        username = browser.find_element_by_id('u')
        password = browser.find_element_by_id('p')
        username.send_keys(qq['username'])
        password.send_keys(qq['password'])
        button = browser.find_element_by_id('go')
        source_url = browser.current_url
        button.click()
        '''这个地方让它睡15s,是因为有时候页面没有跳转或者是页面元素未加载成功，
           可以根据实际网速调整，或者调整代码，改成当元素可达时，进行操作
        '''
        time.sleep(15)
        now_url = browser.current_url
        if source_url == now_url:
            qq_disable.extend(qq)
            # print("账号不能用了,qq:{}".format(qq))
            return
        perf_ssid = dict(browser.get_cookie('perf_ssid')).get('value')
        ubt_ssid = dict(browser.get_cookie('ubt_ssid')).get('value')
        _utrace = dict(browser.get_cookie('_utrace')).get('value')
        snsInfo = dict(browser.get_cookie('snsInfo[101204453]')).get('value')
        cookie = 'perf_ssid={};ubt_ssid={};_utrace={};snsInfo[101204453]={}'.format(perf_ssid, ubt_ssid, _utrace,
                                                                                    snsInfo)
        write_data(cookie)
    except Exception as e:
        print(e)
    finally:
        browser.close()


def get_qq():
    with open(path + '/qq.txt', 'r') as f:
        while True:
            content = f.readline()
            if content == '':
                break
            else:
                txt = content.split('&')
                qq = {}
                qq['username'] = txt[0].strip()
                qq['password'] = txt[1].strip()
                src_qq.append(qq)


def write_data(cookie):
    with open(path + '/cookies.txt', 'a') as f:
        f.write(cookie + '\n')
        f.write('\n')


pool = Pool()
get_qq()
print('总记录数:{}'.format(len(src_qq)))
pool.map(get_cookie, src_qq)
print("失败了{}条".format(len(qq_disable)))
pool.close()
