import requests
from bs4 import BeautifulSoup
import time


class pic:
    def __init__(self, img_add, msg):
        self.__img = img_add
        self.__msg = msg

    def __str__(self):
        return "url:%s,异常:%s" % (self.__img, self.__msg)


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
timeout_url = []


# 获取网页信息
def get_content(page):
    url = "http://weheartit.com/inspirations/taylorswift"
    payload = {'page': page}
    resp = requests.get(url, params=payload,headers=headers)
    if resp.status_code == 200:
        return resp.text
    else:
        return None


# 获取图片地址List
def get_img(content):
    if content is None:
        print("文档地址为空")
        return
    Soup = BeautifulSoup(content, 'lxml')
    imgs = Soup.select("div.grid-responsive > div.col.span-content > div > div > div > div > div > a > img")
    res = list(map(lambda x: x.get("src"), imgs))
    return res


# 下载图片保存到本地
def download_img(img_address):
    try:
        pic = requests.get(img_address, headers=headers, timeout=5, stream=True)
        if pic.status_code == 200:
            with open("/Users/wanpeng/Desktop/imgs/" + str(time.time()).split(".")[0] + ".png", 'wb') as f:
                for chunk in pic:
                    f.write(chunk)
        else:
            print("图片下载失败")
    except Exception as e:
        log(img_address, e)
        return


def log(url, msg):
    timeout_url.append(pic(url, msg))


if __name__ == '__main__':
    for i in range(1, 20):
        content = get_content(i)
        imgs = get_img(content)
        for img in imgs:
            download_img(img)
    else:
        print("下载结束")
    for pic in timeout_url:
        print(pic)

    # download_img("https://data.whicdn.com/images/317561293/superthumb.jpg?t=1534011030")
