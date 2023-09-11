import requests
from bs4 import BeautifulSoup as bs
from requests import Session
s = Session()
import csv
s.headers['user-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'
f = open("apple_pages.csv","w",encoding="utf-8")
# url="https://www.apple.com/shop/accessories/all/made-by-apple"
l=[]
for i in range(1,11):
    url_page = "https://www.apple.com/shop/accessories/all/made-by-apple?page={}".format(i)
    print(url_page)
    r=requests.get(url_page)
    soup = bs(r.content,("html.parser"))
    product=soup.find_all("div","as-producttile-info")
    for i in product:
        e=i.find('a').get("href")
        f.write("https://www.apple.com/"+e+"\n")
    



