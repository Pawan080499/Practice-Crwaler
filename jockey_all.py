from requests import Session
s = Session()
from bs4 import BeautifulSoup as bs
from lxml import html
import pandas as pd

s.headers['Agent-User']="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"

# url='https://www.jockey.in/'

def header_link(url):
    r=s.get(url)
    tree=html.fromstring(r.text)
    head_link= tree.xpath('//div[@class="headerMenu ng-tns-c2-0 ng-star-inserted"]//ul//li')
    head_link= tree.xpath('//nav[@class="navbar navbar-expand-sm"]//ul//li')
    for i in head_link:
        a ='https://www.jockey.in/' + ''.join(i.xpath('.//a/@href'))
        if '/blog' not in a:
            print(a)
            data={
                "link":a,
            }
            l.append(data)
        # print(l)

def list_page(url):
    r=s.get(url)
    tree=html.fromstring(r.text)
    link = tree.xpath('//div[@class="card-body product-card-content"]//a/@href')
    title=tree.xpath('//h5[@class="card-product-title"]//text()')
    price=tree.xpath('//span[@class="product-price"]//text()')
    data={
        "link":link,
        "title":title,
        "price":price,
    }
    listpage.append(data)
    print("Category_Url:- ", url)
    
def detail_page(url, listpage_data=1):
    r=s.get(url)
    tree=html.fromstring(r.text)
    Pro_name=tree.xpath('//h3[@class="pdp_v_productTitle ng-star-inserted"]//text()')
    pro_price=list(set(tree.xpath('//span[@class="mrp-prize mr-2 ng-star-inserted"]//text()')))
    data={
        "title":Pro_name,
        "price":pro_price,
    }
    data.update(listpage_data)
    detailpage.append(data)
    print("Product_Url:- ", url)

l=[]
listpage = []
detailpage = []
header_link('https://www.jockey.in/')

for row in l:
    url = row.get("link")
    list_page(url)

for row in listpage:
    url = row.get("link")
    detail_page(url, row)   
    
df = pd.DataFrame(detailpage)
df.to_excel("jo.csv",index=False)