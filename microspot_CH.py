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
    for j in  soup.find_all("div","wQ1zdx _22abxI _2tZgGy _1ryioq"):
        link = "https://www.microspot.ch"+"".join(j.find("a").get('href'))
        title = j.find('div','_4kaNBc').text
        price = j.find('div','_28doBv').text

        l.append({"Name":title,"URL":link,"Price":price})
        # print(link)
    # for j in tree.xpath('//div[@class="wQ1zdx _22abxI _2tZgGy _1ryioq"]'):
    #     link="https://www.microspot.ch"+''.join(j.xpath('//div[@class="_35THZ2"]//a/@href'))    
    #     title = j.xpath('//div[@class="_4kaNBc"]//text()')
    #     l.append({"Name":title,"URL":link})
   
   
    next_page = ''.join(tree.xpath("//div[@class='INCD3A']//li//button[@class='_3tjBsa _1qTCBs KDDAjc _3GAH1f']//ancestor::a[@class='_16Ool9']//@href")[-1])
    if next_page:
        nxt = "https://www.microspot.ch"+next_page
        crawl(nxt)
    # for g in ''.join(tree.xpath('//div[@class="INCD3A"]//ul//li//a[@class="_16Ool9"]/@href')):
    #     nxt="https://www.microspot.ch"+g
    #     crawl(nxt)

url = "https://www.microspot.ch/de/computer-gaming/notebooks/notebooks--c511000"
crawl(url)

df = pd.DataFrame(l)
df.to_excel("Micropot_CH.xlsx",index=False)