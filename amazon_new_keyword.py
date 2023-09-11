import requests
from bs4 import BeautifulSoup as BS
from lxml import html
import csv
from requests import Session
import pandas as pd
s=Session()
s.headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
all_products = []

def crawling_list_page(response):
    soup = BS(r.content,"html.parser")
    for product in soup.find_all("h2","a-size-mini a-spacing-none a-color-base s-line-clamp-4"):
        d = dict()
        title = product.text.strip()
        prod_url = "https://www.amazon.in"+product.find("a").get("href")
        d["Title"] = title
        d["Product URL"] = prod_url
        all_products.append(d)
        print(f"Product URL :- {prod_url}")
    


url = "https://www.amazon.in/s?k=mommy+pokonpants&page={}&qid=1645708655&ref=sr_pg_{}"
for page in range(1,4):
    r = s.post(url.format(page,page))
    print(r.url)
    crawling_list_page(r)


df = pd.DataFrame(all_products)
df.to_csv("amazon_raw_data.csv",index=False)