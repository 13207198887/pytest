from bs4 import BeautifulSoup
import requests

datas = []

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}


class product():
    def __init__(self, category, title, time, price, quality, area):
        self.__category = category
        self.__title = title
        self.__time = time
        self.__price = price
        self.__quality = quality
        self.__area = area

    def __str__(self):
        return "类别:%s,标题:%s,发布时间:%s,价格:%s,成色:%s,区域:%s" % (
            self.__category, self.__title, self.__time, self.__quality, self.__area)


# 获取页面内容
def get_page(page):
    url = "http://bj.58.com/pbdn/" + str(page) + "/"
    content = requests.get(url, headers=headers)
    if content.status_code != 200:
        print("页面请求失败,url:%s" % (url))
        return
    return content.text


# 获取列表详情页面的数据
def get_xq_list(content):
    Soup = BeautifulSoup(content, 'lxml')
    hrefs = Soup.select("#huishou > tbody > tr > td.t > a")
    print(len(hrefs))
    # hrefs = list(map(lambda x: x.get("href"), ))
    for href in hrefs:
        page_content = requests.get(href, headers=headers)
        if page_content.status_code == 200:
            get_data(page_content.text)
        else:
            print("获取商品详情页失败，href:%s" % (href))


# 获取详情页所需要的数据，并存到数据集中
def get_data(content):
    Soup = BeautifulSoup(content, 'lxml')
    category = Soup.select("#header > div.breadCrumb.f12 > span.crb_i > a")[0].text
    title = Soup.title.text
    time = Soup.select("#index_show > ul.mtit_con_left.fl > li.time")[0].text
    price = Soup.select("li > div.su_con > span")[0].text
    quality = Soup.select("li > div.su_con > span")[1].text.split()[0]
    area = Soup.select("#basicinfo > div.col_sub.sumary.no_col_left > ul > li:nth-of-type(5) > div.su_con")
    datas.append(product(category, title, time, price, quality, area))


if __name__ == '__main__':
    # page = get_page(1)
    # get_xq_list(page)
    # print(datas)
    url = "http://bj.58.com/pingbandiannao/35087919512111x.shtml?psid=193865422201082203818325000&entinfo=35087919512111_0&iuType=p_1&PGTID=0d305a36-0000-1691-c485-402508468eab&ClickID=1"
    content = requests.get(url, headers=headers).text
    get_data(content)
