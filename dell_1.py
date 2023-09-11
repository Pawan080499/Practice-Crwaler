from requests import Session
s = Session()
from bs4 import BeautifulSoup as bs
import pandas as pd
from lxml import html
from pymongo import MongoClient

URI = "mongodb://localhost:27017"
Client = MongoClient(URI)
mydb = Client['Crawling'] ##database name
mycol = mydb['Dell'] ##collection


def craling_list_page(page_no):
    # url="https://www.dell.com/en-in/shop/laptops-2-in-1-pcs/sr/laptops/inspiron-laptops"
    url=f"https://www.dell.com/en-in/shop/laptops-2-in-1-pcs/sr/laptops/inspiron-laptops?page={page_no}"
    r=s.get(url)
    print(r)
    tree=html.fromstring(r.text)
    soup=bs(r.text,"html.parser")
    # link=soup.find_all("div","system-result-product-stack")
    products = tree.xpath("//article")
    print(len(products))
    for product in products:
        # e=i.find('a').get('href')
        # print(e)
        # detail_page(e)
        links= 'https:' + ''.join(product.xpath(".//a[@class='rating-redirect']//@href")).strip()
        # print(links)
        title=''.join(product.xpath(".//h3//text()")).strip()
        # Processor=i.find("span","ps-iconography-specs-label").text.strip()
        Processor="".join(product.xpath(".//div[@class='ps-iconography-specs']//span[contains(string(),'Processor')]//following-sibling::span[@class='ps-iconography-specs-label']//text()")).strip()
        OS="".join(product.xpath(".//div[@class='ps-iconography-specs']//span[contains(string(),'OS')]//following-sibling::span[@class='ps-iconography-specs-label']//text()")).strip()
        Graphics="".join(product.xpath(".//div[@class='ps-iconography-specs']//span[contains(string(),'Graphics')]//following-sibling::span[@class='ps-iconography-specs-label']//text()")).strip()
        Memory="".join(product.xpath(".//div[@class='ps-iconography-specs']//span[contains(string(),'Memory')]//following-sibling::span[@class='ps-iconography-specs-label']//text()")).strip()
        Storage="".join(product.xpath(".//div[@class='ps-iconography-specs']//span[contains(string(),'Storage')]//following-sibling::span[@class='ps-iconography-specs-label']//text()")).strip()
        Display="".join(product.xpath(".//div[@class='ps-iconography-specs']//span[contains(string(),'Display')]//following-sibling::span[@class='ps-iconography-specs-label']//text()")).strip()
        
        # all_products.append()
        # print(all_products)
        dt = {"url":links,"title":title,"processor":Processor,"os":OS,"Graphic":Graphics,"Memory":Memory,"storage":Storage,"display":Display}
        try:
            mycol.insert_one(dt)
        except:
            pass
    
    
# for page in range(1,4):
#     print(page)
#     r=s.get(f"https://www.dell.com/en-in/shop/laptops-2-in-1-pcs/sr/laptops/inspiron-laptops?page={page}")
#     next_page=soup.find_all("div","horizontal-layout")
#     for i in next_page:
#         pro_url=i.find('a').get('href')
#         print(pro_url)

all_products=[]
for i in range(1,5):
    craling_list_page(i)
    
        
        
    

# df=pd.DataFrame(all_products)
# df.to_excel("dell_1_new.xlsx",index=False)
    
    
    