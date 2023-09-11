from requests import Session
s = Session()
from bs4 import BeautifulSoup as bs
from lxml import html
import pandas as pd

s.headers['User-Agent']="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
# url="https://www.fcomputer.dk/computer/baerbar?"
l=[]

def crawl_data(url):
    r=s.get(url)
    soup=bs(r.text,'html.parser')
    tree=html.fromstring(r.text)
    for i in soup.find_all("div","related-product-list-wrapper desktop-4-100"):
        link=i.find('a').get('href')
        title=soup.find('div','product-header').text.replace("\n","")
        a=i.find('div','product-header').find('span')
        if a:
            a = i.find('div','product-header').find('span').text
        else:
            a = "not found"
        b=b=i.find('span','product-subheader')
        if b:
            b = i.find('span','product-subheader').text
        else:
            b = "not found"
        title=a+b
        
        # product_name=i.find('div','bottom-name-wrapper')
        # if product_name: 
        #     product_name = i.find('div','bottom-name-wrapper').text.split()[1]
        # else:
        #     product_name = "not found"
            
        # EAN=i.find('div','bottom-name-wrapper')
        # if EAN:
        #     EAN = i.find('div','bottom-name-wrapper').text.split()[3]
        # else:
        #     EAN = "not found"
        # Varenummer=i.find('div','bottom-name-wrapper')
        # if Varenummer:
        #     Varenummer = i.find('div','bottom-name-wrapper').text.split()[5]
        # else:
        #     Varenummer = "not found"
        
        l.append({"link":link,"title":title})
        # print(l)
        
    next_page = ''.join(tree.xpath('//nav[@id="category-pagination"]//ul//li[@aria-label="Next"]//a/@href'))
    if next_page:
        nxt= "https://www.fcomputer.dk/computer/baerbar"+next_page
        print(nxt)
        crawl_data(nxt)
        
    
        
url = "https://www.fcomputer.dk/computer/baerbar?page=1"
crawl_data(url)

df = pd.DataFrame(l)
df.to_excel("comp.xlsx",index=False)


