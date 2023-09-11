import requests
from requests import Session
s = Session()
import json
import pandas as pd
from lxml import html
# from bs4 import BeautifulSoup as b

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'x-algolia-api-key': '0e7364c3b87d2ef8f6ab2064f0519abb',
    'x-algolia-application-id': 'XN5VEPVD4I',
    'content-type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.fashionnova.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.fashionnova.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
}

data = '{"query":"","userToken":"anonymous-e48cc2c6-5c63-47d6-bc83-fe676f895058","ruleContexts":["collection","one-piece"],"analyticsTags":["collection","one-piece","desktop","Returning","India"],"clickAnalytics":true,"distinct":1,"page":0,"hitsPerPage":48,"facetFilters":["collections:one-piece"],"facetingAfterDistinct":true,"attributesToRetrieve":["handle","image","title"],"personalizationImpact":0}'

response = requests.post('https://xn5vepvd4i-dsn.algolia.net/1/indexes/products/query?x-algolia-agent=Algolia%20for%20JavaScript%20(4.14.2)%3B%20Browser',headers=headers,data=data,)
# s.headers.update(headers)

js=response.json()
l=[]
tree=html.fromstring(response.text)
def list_page(url):
    product=js['hits']
    for i in product:
        pro_url=i.get('handle')
        title=i.get('title')
        image=i.get('image')
        # print(image)
        # print("https://www.fashionnova.com/products/"+pro_url)
        data={
            "pro_url" : "https://www.fashionnova.com/products/"+pro_url,
            "title" : title,
            "image" : image,
        }
        l.append(data)
        print(l)
        
url="https://www.fashionnova.com/collections/one-piece"
for i in range(1,3):
    # data['pag'] = i
    r=requests.get(url.format(i))
    list_page(url)
    print(data)

    # next_page = ''.join(tree.xpath('//div[@class="pagination__group"]//ul//li[@class="pagination__next-cta"]//a/@href'))
    # if next_page:
    #     nxt = "https://www.fashionnova.com/collections/one-piece?"+next_page
    #     print(nxt)
    #     list_page(nxt)


url="https://www.fashionnova.com/collections/one-piece?page=1"
list_page(url)    
        
df = pd.DataFrame(l)
df.to_excel("fashion.xlsx",index=False)
