from requests import Session
s = Session()
from bs4 import BeautifulSoup as bs
import pandas as pd
s.headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
s = Session()
l=[]
for i in range(1,100):
    url="https://www.jiomart.com/c/fashion/women/493?prod_mart_fashion_products_popularity%5Bpage%5D={}&prod_mart_fashion_products_popularity%5Brange%5D%5Bavg_discount_pct%5D=20%3A".format(i)
    response = s.get(url.format(i))
    soup = bs(response.content,"html.parser")
    links=soup.find_all("a","category_name prod-name")
    for link in links:
         e=link.get('href')
         print(e)
         l.append({"links":"https://www.jiomart.com"+e})
        #  print(response.status_code)
    # print(i, '...............')
    
    df=pd.DataFrame(l)
    df.to_excel("jiomart.xlsx",index=False)

  
