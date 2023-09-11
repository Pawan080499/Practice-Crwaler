import requests
from requests import Session
import csv
from bs4 import BeautifulSoup as bs
s = Session()
s.headers['user-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'
f = open("flipkat_links.csv","w",encoding="utf-8")
writer = csv.writer(f)
writer.writerow(["Links"])
url="https://www.flipkart.com/clothing-and-accessories/topwear/pr?sid=clo%2Cash&p%5B%5D=facets.ideal_for%255B%255D%3DMen&p%5B%5D=facets.ideal_for%255B%255D%3Dmen&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_f70fae18-a2dc-47a9-87e4-2b6899ed8182_1_372UD5BXDFYS_MC.AHHHWF67UPNB&otracker=hp_rich_navigation_1_1.navigationCard.RICH_NAVIGATION_Fashion%7EMen%2527s%2BTop%2BWear%7EAll_AHHHWF67UPNB&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L2_view-all&cid=AHHHWF67UPNB&page={}"
l = []
for i in range(1,31):
    r=requests.get(url.format(i))
    soup=bs(r.content,"html.parser")
    products=soup.find_all("a","_2UzuFa")
    for product in products: 
        # l.append(i.get("href"))
        link = "https://www.flipkart.com"+str(product.get("href")).strip()
        writer.writerow([link])
    print(link)

