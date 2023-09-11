import requests
from requests import Session
s = Session()
import pandas as pd
from bs4 import BeautifulSoup as bs

data = list()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Origin': 'https://bluebungalow.com.au',
    'Connection': 'keep-alive',
    'Referer': 'https://bluebungalow.com.au/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

def detail_page(url):
    item = dict()
    r = s.get(url)
    soup = bs(r.text, features='lxml')
    title = soup.find("h1")
    item["product_url"] = url
    item["title"] = title.text.strip()
    item["price"] = soup.text
    item["description"]=soup.find("div","product-tabs-content-inner clearfix").text.strip()
    item["shiping"]=soup.find("div",id="tab1533810939652").text.strip()
    print(item)
    data.append(item)
    
    
    


for page in range(0,60,30):
    print(page)
    r=s.get(f"https://search.unbxd.io/ac541912a18c803bfeab27f04ccbebf4/prod-bluebungalow-au4941591590495/category?&rows=30&start={page}&p=categoryPath%3A%22shoes%22&format=json&view=grid&stats=price&fields=title,uniqueId,collection_tag,plain_tags,publishedAt,secondaryImageUrl,documentType,imageUrl,price,sellingPrice,priceMax,sku,imageUrl,sizeMap,relevantDocument,productUrl,variantId,brand,availability,altImageUrl,altImageTag,imageList&facet.multiselect=true&pagetype=boolean&version=V2&indent=off&filter=documentType:product&filter=publishedAt:*&device-type=Desktop&unbxd-url=https%3A%2F%2Fbluebungalow.com.au%2Fcollections%2Fshoes&unbxd-referrer=https%3A%2F%2Fbluebungalow.com.au%2F&user-type=new&api-key=ac541912a18c803bfeab27f04ccbebf4")
    js=r.json()
    s.headers.update(headers)
    product=js['response']['products']
    l=[]
    for i in product:
        pro_url="https://bluebungalow.com.au"+i.get('productUrl')
        detail_page(pro_url)
        # title=i.get('title')
        # brand=i.get('brand')
        # price=i.get('price')
        # image=i.get('imageUrl')
        # size=i.get('sizeMap')
        # # print(pro_url)
        # data={
        #     'pro_url' : pro_url,
        #     'title' : title,
        #     'brand' : brand,
        #     'price' : price,
        #     'image' : image,
        #     'size' : size
        # }
        
        # l.append(data)
        # print(l)
            
df=pd.DataFrame(data)
df.to_excel("blue.xlsx",index=False)
    