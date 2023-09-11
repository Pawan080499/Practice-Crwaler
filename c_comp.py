import requests
from bs4 import BeautifulSoup as bs
from requests import Session
s = Session()
from lxml import html
import csv
import pandas as pd
# import mysql.connector
# conn = mysql.connector.connect(host ='localhost',  user = 'root', passwd = 'root', db = 'company')
# cursor = conn.cursor()

s.headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
url="https://www.fcomputer.dk/computer/baerbar"

l=[]
def crawl(url):
	r=s.get(url)
	print(url)
	soup=bs(r.content,"html.parser")    
	# tree=html.fromstring(r.text) 
	for i in soup.find_all("div","related-product-list-wrapper desktop-4-100"):
		link="".join(i.find("a").get("href"))
		title= i.find("span","product-header").text.replace("\n\n","").replace("\n","")
		img=i.find("img","img-responsive lazy").get('data-src')

		# query = 'insert into c_com(link,title,img) values(%s,%s,%s)'
		# values = [link,title,img]
		# cursor.execute(query,values)
		# conn.commit()

		l.append({"url":link,"name":title,"Img":img}) 
                                                         
	next_page = soup.find("div","left-product-list-headers-wrapper").find('a').get('href')
	if next_page:
		nxt = "https://www.fcomputer.dk/computer/baerbar"+next_page
		crawl(url)

crawl(url)
df = pd.DataFrame(l)
df.to_excel("c_comp.xlsx",index=False)
