from bs4 import BeautifulSoup
import requests
# path = "/User/wanpeng/Desktop/xiaozhu.htm"
url = 'https://nj.xiaozhu.com/fangzi/18675103203.html';
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
title = soup.select('div.pho_info > h4 > em')
address = soup.select('div.pho_info > p > span')
img = soup.select('#imgMouseCusor')
price = soup.select('#pricePart > div.day_l > span')
master_name = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
master_sex = soup.select('<span class="member_boy_ico"></span>')
code = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > p > span.zm_ico.zm_credit')

data = {

    'url':url.text
}
