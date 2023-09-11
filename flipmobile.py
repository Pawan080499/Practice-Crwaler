from telnetlib import STATUS
from urllib import request
from requests import Session
s = Session()
from bs4 import BeautifulSoup as bs
import pandas as pd
s.headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
s = Session()
# f=open("filpmobile.csv","w",encoding="utf-8")
l=[]
for i in range(1,5):
    url_page="https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=9ed621dd-c671-46d5-8507-a34274a68196&as-backfill=on&page={}".format(i)
    print(url_page)
    r=s.get(url_page)
    print(r.status_code)
    soup=bs(r.content,"html.parser")
    link=soup.find_all("div","_2kHMtA")
    for i in link:
        e=i.find('a').get('href')
        # f.write("https://www.flipkart.com/"+e+"\n")
        l.append({"links":"https://www.flipkart.com"+e})
    
    df=pd.DataFrame(l)
    df.to_excel("moblie.xlsx",index=False)
    
    #  for i in range(1,41):
    #      print(url.format(i))
    #      f.write(url.format(i)+"\n")
    
    