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
    for j in  soup.find_all('div','search-results-list-item'):
        link = "".join(j.find("h2").find('a').get('href'))
        title = j.find('h2').find('a').text
        if j.find('img'):
            image = j.find('img').get('data-src')
        else:
            image = "Not given"
        price = j.find('div','product-pricing').find('span').text

        l.append({"Name":title,"URL":link,"price":price,"image":image})
   
    try:
        next_page = ''.join(tree.xpath('//div[@class="pagination-container"]//ul//li[@class="pagination-next navigate"]//a/@href')[1])
        if next_page:
            nxt = next_page
            crawl(nxt)
    except:
        pass

url = "https://www.uk.insight.com/en-gb/searchresults/computers/desktop-pcs?FK%5B%5D=&slider_selected_low_price=100&slider_selected_high_price=7800&slider_low_price=100&slider_high_price=7800&currency_format=%C2%A30&LP=100&HP=7800&A-DAX-ManufacturerID%5B%5D=51513&C=C-1013&lang=en-gb&RF%5B%5D=&SB=bs&PS=10&P=1&all=y"
crawl(url)

df = pd.DataFrame(l)
df.to_excel("insight_UK.xlsx",index=False)