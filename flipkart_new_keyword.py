import requests
from bs4 import BeautifulSoup as BS
from lxml import html
import csv
from requests import Session
import pandas as pd
#import mysql.connector
s=Session()
s.headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
all_products = []

# conn = mysql.connector.connect(host='localhost',user='root', passwd='root', db='company')
# cursor = conn.cursor()


def crawling_list_page(response):
    soup = BS(r.content,"html.parser")
    for product in soup.find_all("div","_4ddWXP"):
        d = dict()
        title = product.find("a","s1Q9rs").text
        prod_url = "https://www.flipkart.com"+product.find("a","s1Q9rs").get("href")
        d["Title"] = title
        d["Product URL"] = prod_url
        # all_products.append(d)
        
        # query = 'insert into product(title,url) values(%s,%s)'

        # values = [title,prod_url]
        # cursor.execute(query,values)
        # conn.commit()

        print(f"Product URL :- {prod_url}")
    


url = "https://www.flipkart.com/search?q=mommy+pokonpants&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={}"
for page in range(1,10):
    r = s.get(url.format(page))
    print(r.url)
    crawling_list_page(r)


df = pd.DataFrame(all_products)
df.to_csv("Flipkart_raw_data.csv",index=False)