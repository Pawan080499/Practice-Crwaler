import requests
from requests import Session
import csv
from bs4 import BeautifulSoup as bs
s = Session()
s.headers['user-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'
f = open("flipkat_links.csv","w",encoding="utf-8")
writer = csv.writer(f)
#writer.writerow(["Links"])
url="https://www.flipkart.com/watches/pr?sid=r18&otracker=product_breadCrumbs_Watches&page=24"
l=[]
for i in range(1,29):
    r=requests.get(url.formate(i))
    soup=bs(r.content,"html.parser")
    product=soup.find_all("div","_13oc-S _1t9ceu")
    for products in product:
        link=("https://www.flipkart.com"+str(products.get("href"))).strip()
        # writer.writerow([link])
    # print(i)
    










