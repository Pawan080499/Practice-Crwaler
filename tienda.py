import requests
from bs4 import BeautifulSoup as BS
from lxml import html
import csv
from requests import Session
import pandas as pd
s=Session()
s.headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'

l=[]
def crawl(url):
    r=s.get(url)
    print(url)
    soup=BS(r.content,'html.parser')
    tree = html.fromstring(r.text)
    for j in  soup.find_all('li','item'):
        link = "".join(j.find("a").get('href'))
        title = ''.join(j.find('div','product-name').text).strip()
        image = j.find('img').get('src')
        oldprice = ''.join(j.find('p','old-price').text).strip()
        newprice = ''.join(j.find('p','special-price').text).strip()

        l.append({"Name":title,"URL":link,"image":image,"oldprice":oldprice,"newprice":newprice})
   
   
    next_page = ''.join(set(tree.xpath('//div[@class="pages"]//a[@class="fa fa-angle-right next i-next"]/@href')))
    if next_page:
        nxt = next_page
        crawl(nxt)


url = "https://www.tiendalenovo.es/tablet/tablets-hogar/tablet-android-tab"
crawl(url)

df = pd.DataFrame(l)
df.to_excel("tiendalenovo_es.xlsx",index=False)