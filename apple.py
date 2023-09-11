import requests
from bs4 import BeautifulSoup as bs
from requests import Session
s = Session()
import csv
s.headers['user-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'
f = open("apple.csv","w",encoding="utf-8")
url="https://www.apple.com/shop/accessories/all/made-by-apple"
r=requests.get(url)
soup = bs(r.content,("html.parser"))
product=soup.find_all("div","as-producttile-info")
l=[]
for i in product:
    e=i.find('a').get("href")
    f.write("https://www.apple.com/"+e+"\n")



