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
    #print(url)
    # print(r.status_code)
    soup=BS(r.content,'html.parser')
    tree = html.fromstring(r.text)
    for j in soup.find_all("div","related-product-list-wrapper desktop-4-100"):
        link = "".join(j.find("a").get('href'))
        # title = j.find('span','product-header').text
        # img = j.find('source').get('data-srcset')

        l.append({"link":link})
   
   
    next_page = ''.join(tree.xpath('//nav[@id="category-pagination"]//ul//li[@aria-label="Next"]//a/@href'))
    if next_page:
        nxt = "https://www.fcomputer.dk/computer/baerbar?"+next_page
        print(nxt)
        crawl(nxt)


url = "https://www.fcomputer.dk/computer/baerbar?page=1"
crawl(url)  

df = pd.DataFrame(l)
df.to_excel("Fcomputer_dk.xlsx",index=False)