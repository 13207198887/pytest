import time
import requests
import os
from bs4 import BeautifulSoup
from chromeDriver import Chrome
from multiprocessing import Pool
from mongo_driver import MongoDB
from multiprocessing import Manager

'''详情页面有反爬机制，只能用selenium来解决啦'''

'''headers'''
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Cookie': "mediav=%7B%22eid%22%3A%22387123%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22%25%3FIwfwO0yY%3C%2B%3A3J70%3DGf%22%2C%22ctn%22%3A%22%22%7D; _channel=other_google; _keyword=; _caid=; __jsluid=ad74a7ed55f98e0895e1272a41cfea5f; mayi_uuid=5749033260853621454185; _my_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%7D; sid=759309608911416; Hm_lvt_0294bbb72b1c6a6b342da076397c9af2=1534511131; _caname=""; accessId=73859f20-f357-11e6-b43e-3b18b16942dc; _ga=GA1.2.716877030.1534511131; _gid=GA1.2.54171913.1534511131; bad_id73859f20-f357-11e6-b43e-3b18b16942dc=3897ef41-a21e-11e8-9e5c-8dadf9d3fc83; nice_id73859f20-f357-11e6-b43e-3b18b16942dc=3897ef42-a21e-11e8-9e5c-8dadf9d3fc83; searchkey=%u6DF1%u5733%2C%u5E7F%u4E1C%u7701%26/shenzhen/%262%261534511137790; serInfo_back_PC=%26_%26_%26_%26_0%u665A_%26; cto_lwid=813a2176-9dbd-4e72-addd-65307dd8de3b; MAYI_SDTC_T=sdtc; Qs_lvt_101147=1534513646; qimo_seosource_73859f20-f357-11e6-b43e-3b18b16942dc=%E7%AB%99%E5%86%85; qimo_seokeywords_73859f20-f357-11e6-b43e-3b18b16942dc=; sdtan=1; SESSION=010dd5a8-c67f-42b4-a514-cc6867e117af; __jsl_clearance=1534515095.866|0|eFl4GmrBilG324I%2B5Q6tzW%2BxUTE%3D; _ip=183.240.33.178; _historys=853141513%3DD5%u8FD1DSN%u4E50%u56ED/%u514D%u8D39%u63A5%u9001/%u7D2B%u7F57%u51702%u5C45%3D300%3Dhttps%3A//i1.mayi.com/mayi75/M51/QE/RM/NZPDWH598DQ2BNHT5G7Q6WR9WVTF77.jpg_90x60c.jpg%26850553418%3D%u91D1%u9E70%u9A8F%u8C6A%u516C%u5BD3%u8C6A%u534E%u5957%u623F%u8212%u9002%u5BBD%u655E%u5357%u4EAC%u897F%u8DEF%u6CBF%u7EBF%3D566%3Dhttps%3A//i1.mayi.com/mayi77/M60/FR/VA/DGUKT97BHV323UV98W2RKJDFUUBXTH.jpg_90x60c.jpg%26850553418%3D%u91D1%u9E70%u9A8F%u8C6A%u516C%u5BD3%u8C6A%u534E%u5957%u623F%u8212%u9002%u5BBD%u655E%u5357%u4EAC%u897F%u8DEF%u6CBF%u7EBF%3D566%3Dhttps%3A//i1.mayi.com/mayi77/M60/FR/VA/DGUKT97BHV323UV98W2RKJDFUUBXTH.jpg_90x60c.jpg%26853141513%3DD5%u8FD1DSN%u4E50%u56ED/%u514D%u8D39%u63A5%u9001/%u7D2B%u7F57%u51702%u5C45%3D300%3Dhttps%3A//i1.mayi.com/mayi75/M51/QE/RM/NZPDWH598DQ2BNHT5G7Q6WR9WVTF77.jpg_90x60c.jpg%26853141513%3DD5%u8FD1DSN%u4E50%u56ED/%u514D%u8D39%u63A5%u9001/%u7D2B%u7F57%u51702%u5C45%3D300%3Dhttps%3A//i1.mayi.com/mayi75/M51/QE/RM/NZPDWH598DQ2BNHT5G7Q6WR9WVTF77.jpg_90x60c.jpg%26853141513%3DD5%u8FD1DSN%u4E50%u56ED/%u514D%u8D39%u63A5%u9001/%u7D2B%u7F57%u51702%u5C45%3D300%3Dhttps%3A//i1.mayi.com/mayi75/M51/QE/RM/NZPDWH598DQ2BNHT5G7Q6WR9WVTF77.jpg_90x60c.jpg; Hm_lpvt_0294bbb72b1c6a6b342da076397c9af2=1534515116; viewhistory=*853141513*850553418; Qs_pv_101147=496085451354610100%2C284697834137655700%2C3895649695604653600%2C3899301120031706000%2C1623941556361573400; pageViewNum=13",
    'X-Requested-With': 'XMLHttpRequest'
}

'''定义一个item'''
item = {}
path = os.path.join(os.path.expanduser("~"), "Desktop")
mgr = Manager()
url_list = mgr.list()
'''获取mongo连接'''
mongo = MongoDB()


## 获取url列表
def get_url_list(page, area="shanghai"):
    url = 'https://www.mayi.com/{}/{}'.format(area, page)
    page_text = requests.get(url, headers=headers).text
    soup = BeautifulSoup(page_text, 'lxml')
    htmls = soup.select(".house-image > a:nth-of-type(1)")
    url_list.extend(list(map(extend_url, htmls)))


## 根据data拼接url
def extend_url(data):
    no = data.get("data")
    return "https://www.mayi.com/room/{}/".format(no)


## 获取详情页面的html
def get_item_html(url):
    no = url.split("/")[-2]
    '''干掉重复的'''
    if nos.count(no) > 0:
        return
    chrome = Chrome()
    driver = chrome.get_driver();
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    driver.close()
    write_no(no)
    write_html(no, html)


def analysis_and_store_item(no):
    with open(path + '/mayi/{}.html'.format(no), 'r') as f:
        html = f.read()
        soup = BeautifulSoup(html, 'lxml')
        item = {}
        item['no'] = no
        item['title'] = soup.select('.desWord > h2 > a:nth-of-type(1)')[0].text
        item['address'] = soup.select('.desWord > p')[0].text.rsplit('查看地图')[0]
        item['imgs'] = list(map(lambda x: 'http:' + x.get('src'), soup.select('.piclist > li > a > img')))
        item['info'] = soup.select('.feature > ul > li:nth-of-type(1) > p')[0].text
        item['price'] = soup.select('#priceL > span')[0].text
        '''存数据库'''
        store_item(item)


def store_item(item):
    client = mongo.get_client()
    db = mongo.get_database(client, "mayi")
    tb = mongo.get_table(db, "room")
    if tb.find_one({'no': item['no']}) is None:
        tb.insert_one(item)
    client.close()


# soup = BeautifulSoup(html, 'lxml')
# title = soup.select(".desWord > h2 > a:nth-of-type(1)")[0].text()
# print( no,title)

def write_html(no, html):
    with open(path + '/mayi/{}.html'.format(no), 'a') as f:
        f.write(html)


def write_no(no):
    with open(path + '/mayi/no.txt', 'a') as f:
        f.write(no)
        f.write('\n')


'''从文件中读取已存在的'''
nos = []
with open(path + '/mayi/no.txt', 'r+') as f:
    while True:
        line = f.readline()
        if len(line) != 0:
            nos.append(line.strip())
        else:
            break

pool = Pool()
'''爬取1到10页'''
# pages = [x for x in range(1, 11)]
# pool.map(get_url_list, pages)
# pool.map(get_item_html, url_list)
# pool.close()

'''处理页面文件,抓取需要的数据'''
pool.map(analysis_and_store_item, nos)
