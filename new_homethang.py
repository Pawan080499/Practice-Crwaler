from requests import Session
s = Session()
from bs4 import BeautifulSoup as BS
# s.headers['user-agent']="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0"
import pandas as pd
list1=[]


def crawl_all_category (url):
    r=s.get(url)
    soup=BS(r.text,'html.parser')
    for i in soup.find_all('div','category-list'):
        sub='https://www.homethangs.com/'+i.find('a').get('href')
        print('main_sub',sub)
        sub_category1(sub)

def sub_category1(url):
    r=s.get(url)
    soup=BS(r.text,'html.parser')
    product = soup.find_all('table','categoryitem')
    if product:
        print("-----------------",url)
        listpage_links.append(url)

    for i in soup.find_all('div','category-list'):
        sub_all = 'https://www.homethangs.com/'+i.find('a').get('href')
        # print('2nd_sub',sub_all)
        sub_category1(sub_all)

def list_page(url,page):
    r=s.get(url.format(page))
    print(r.url)
    soup=BS(r.text,'html.parser')

    products = soup.find_all('table','categoryitem')
    if products:
        for i in products:
            product_url=i.find('a').get('href')
            print("https://www.homethangs.com/"+url)
            name=i.find("p","h1-link").text
            if i.find('b').find('span'):
                rate=(i.find('b').find('span').text.strip())
            else:
                rate = ''
            details=i.find('p','h1-link').text
            image=i.find('a').find('img').get('src')
            item=dict()
            item['landingpage_url'] = r.url
            item['url'] = "https://www.homethangs.com/"+product_url
            item['title'] = name
            item['price'] = rate
            item['Details'] = details
            item['Image_link'] = image
            list1.append(item)
            # print(item)
        page+=1
        if int(soup.find('div','hql-total-page').text.split(' 1 of ')[1])>=page:
            # list_page(url,page)
            next_url = url.split('&page')[0] + '&page={}'
            # print("Next page url :- {}".format(next_url))
            list_page(next_url,page)
    

# listpage_links = []
# crawl_all_category("https://www.homethangs.com/bathroom-320.html")

# for url in listpage_links:
#     list_page(url,page=1)
    # print(list_page)

listpage_links =  ['https://www.homethangs.com/steam-bath-generators-467.html']
for url in listpage_links:
    url = url + '&page={}'
    list_page(url,page=1)

df = pd.DataFrame(list1)
df.to_excel("homethang.xlsx",index=False)
print(list1)




# https://www.youtube.com/watch?v=m-koIYWCaIo
# https://www.youtube.com/watch?v=4VfqVpTz4Q4    using function