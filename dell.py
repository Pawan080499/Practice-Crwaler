from requests import Session
from bs4 import BeautifulSoup as bs
s = Session()
import pandas as pd
l=[]
url="https://www.dell.com/en-in/shop/deals/deals"
r=s.get(url)
soup=bs(r.content,"html.parser")
product=soup.find_all("h3","ps-title")
for i in product:
    links=i.find('a').get('href')
    title=i.find("h3","ps-title").text.strip()
    mrp=i.find("div","ps-dell-price ps-simplified").text.strip().replace("Dell Price\n","")
    specification=i.find("div","iconography-feature-specs").text.strip().replace("\n\n\n","").replace("\n","")
    model=i.find("div","ps-desc").text.strip()
    special_offer=i.find("div","ps-offers ps-offers-expanded").find('ul').text.strip().replace("\n\n\n","").replace("\n","")
    
    l.append({"urls":links,"title":title,"MRP":mrp,"specification":specification,"model":model,"special_offer":special_offer})
    

    df=pd.DataFrame(l)
    df.to_excel("Dell.xlsx",index=False)
    