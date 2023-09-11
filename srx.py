from requests import Session
s = Session()
from bs4 import BeautifulSoup as bs
url="https://www.srx.com.sg/singapore-property-listings/hdb-for-sale"


s.headers['User-Agent']="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
r=s.get(url)
soup=bs(r.text,"html.parser")
link=soup.find_all('div','row listingTitleRow')
for i in link:
    e=i.find('a').get('href')
    title=i.find('span','notranslate').text
    build_date=i.find('div','listingDetailType').text.strip()
    
    squar_feet=i.find('div','listingDetailValues').text.strip()
    price=i.find('div','listingDetailPrice adjusted-line-height').text.strip()
    # print("https://www.srx.com.sg"+e)
    d={
        "title":title,
        "build_date":build_date,
        "squar_feet":squar_feet,
        "price":price
    }
    
    print(d)
# def details_page(url):
#     r=s.get(url)
#     soup=bs(r.text,"html.parser")
    
    
    
    