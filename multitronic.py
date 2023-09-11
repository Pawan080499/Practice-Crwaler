import requests
from bs4 import BeautifulSoup as BS
from lxml import html
# import csv
from requests import Session
import pandas as pd
import json
# import mysql.connector
# conn = mysql.connector.connect(host='localhost', user='root',passwd='root',db='company')
# cursor = conn.cursor()
s=Session()

s.headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
l=[]

def crawl(r):
	tree = html.fromstring(r.text)
	soup = BS(r.content,"html.parser")
	print(r.url)
	for j in  soup.find_all("div","listThumbWrapper"):
		link = "https://www.multitronic.fi"+"".join(j.find("a").get('href'))
		title = j.find('a','pTitle pcTracker').text

		# query = 'insert into multitronic(link,title) values(%s,%s)'
		# values = [link,title]
		# cursor.execute(query,values)
		# conn.commit()

		l.append({"Name":title,"URL":link})



data = {
	"sort": "8",
	"sel": "0",
	"dir": "asc",
	"keywords": "",
	"page": "2",
	"ppp": "24",
	"fs": "false",
	"express": "false",
	"man": "164",
	"cats": "",
	"condition_groups": "",
	"view": "2",
	"sf": "true",
	"pag": "",
	"shop_stocks": "",
	"delivery_times": "",
	"as": "#filter",
	"getall": "true"
}
url = "https://www.multitronic.fi/en/category/getfiltersanddata/id/276"
for i in range(1,30):
	data['pag'] = i
	r = s.post(url,data=json.dumps(data))
	crawl(r)
	print(data["pag"])

df = pd.DataFrame(l)
df.to_excel("multitronic_fi.xlsx",index=False)