from requests import Session
from bs4 import BeautifulSoup as bs
import pandas as pd
s = Session()
l=[]
url="https://www.yellow-pages.ph/search/wherehouse/nationwide/page-1"
r=s.get(url)
soup=bs(r.content,"html.parser")
product=soup.find_all("div","search-listing")
for j in product:
    # e=i.find("a").get("href")
    # print("https://www.yellow-pages.ph"+e+"/n")
    links="".join("https://www.yellow-pages.ph"+j.find("a").get('href'))
    title=j.find("h2","search-tradename").text.strip() 
    subtitle=j.find("h3","search-businessname").text.strip()    
    rating=j.find("div","search-rating-container").text.strip().replace("\n","")
    address=j.find("span","ellipsis").text
    # email=j.find("a","biz-link d-block ellipsis yp-click email-link").text
    
    l.append({"url":links,"name":title,"Rate":rating,"Adress":address,"name2":subtitle})
    
    
    df=pd.DataFrame(l)
    df.to_excel("yellopage.xlsx",index=False)