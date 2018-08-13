from bs4 import BeautifulSoup

with open('/Users/wanpeng/Desktop/index.html','r') as wb_data:
    Soup = BeautifulSoup(wb_data,'lxml')
    #print(Soup)
    srcs = Soup.select('body > div > div > div.col-md-9 > div:nth-of-type(2) > div > div > img')
    titles = Soup.select('body > div > div > div > div > div > div > div > h4 > a')
    prices = Soup.select('body > div > div > div.col-md-9 > div:nth-of-type(2) > div > div > div > h4.pull-right')
    stars = Soup.select('body > div > div > div.col-md-9 > div:nth-of-type(2) > div > div > div.ratings > p:nth-of-type(2)')
    reviews = Soup.select('body > div > div > div > div > div > div > div > p.pull-right')

    #print(srcs,titles,prices,reviews,sep='\n-----\n')
for src,title,price,star,review in zip(srcs,titles,prices,stars,reviews):
    data = {
        'src':src.get('src'),
        'title':title.get_text(),
        'price':price.get_text(),
        'star':len(star.find_all("span",class_='glyphicon glyphicon-star')),
        'review':review.get_text()
        }
    print(data)

