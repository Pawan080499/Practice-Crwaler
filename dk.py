from requests import Session
s = Session()
from bs4 import BeautifulSoup as bs
from lxml import html

s.headers['User-Agent']="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
l=[]
url="https://www.fcomputer.dk/"
def Main_headers(url):
    r=s.get(url)
    # soup=bs(r.text,"html.parser")
    tree=html.fromstring(r.text)
    link=tree.xpath("//div[@class='navbar-collapse collapse']//li//a")
    for i in link:
        links="https://www.fcomputer.dk"+i.get('href')
        print(links)
        
Main_headers(url)

