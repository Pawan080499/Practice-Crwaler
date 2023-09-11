import requests
from bs4 import BeautifulSoup as BS
from lxml import html
import csv
from requests import Session
import pandas as pd
s=Session()
s.headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'

l=[]
def crawl(url):
    r=s.get(url)
    #print(url)
    print(r.status_code,"zivame.com")
    soup=BS(r.content,'html.parser')
    tree = html.fromstring(r.text)
    for j in soup.find_all("div","front pos-relative"):
        link = "".join(j.find("a").get('href'))
        title = j.find('h1','text()').text                           #title=tree.xpath("//h1//text()")
        img = j.find('source').get('data-srcset')

        l.append({"Name":title,"URL":link,"Img":img})
   
   
    next_page = ''.join(tree.xpath('//nav[@id="category-pagination"]//ul//li[@aria-label="Next"]//a/@href'))
    if next:
        nxt = "https://www.zivame.com/search/result?trksrc=search&trkid=formsubmit&q=shirt"+next_page
        crawl(nxt)


url = "https://www.zivame.com/search/result?trksrc=search&trkid=formsubmit&q=shirt&page=1"
crawl(url)  

df = pd.DataFrame(l)
df.to_excel("ziv.xlsx",index=False)