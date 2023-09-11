import requests
from requests import Session
s = Session()
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

cookies = {
    '_gaexp': 'GAX1.2.nr2c3GE4S7yNtDc8v1RXpg.19349.1!RT-H9pSzT_SrFt4W13rv7g.19393.1!wnRXqZWOSEqho9JMFw_FvA.19403.1!PeTJGbW1QZSlhSATi8Xbtw.19428.1!ixTmMHm5Qf6wJvC0cRUkqQ.19364.0',
    'V': '201',
    '_gcl_au': '1.1.963077808.1671189846',
    'sessionStatus': 'true|undefined',
    'FirstPage': 'Fri Dec 16 2022 16:54:48 GMT+0530 (India Standard Time)',
    'AB': 'B',
    '_ga': 'GA1.2.2009134722.1671189846',
    '_gid': 'GA1.2.1532272683.1671189846',
    '_fbp': 'fb.1.1671189846479.835917552',
    '_fpuuid': 'Qusczw-1F8PHB7H-Cxi2k',
    'ImpressionCookie': '0',
    'cdigiMrkt': 'utm_source%3A%7Cutm_medium%3A%7Cdevice%3Ad%7Cexpires%3ASun%2C%2015%20Jan%202023%2011%3A24%3A48%20GMT%7C',
    '_dc_gtm_UA-68002030-1': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.ajio.com/s/boys-denims-trousers',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
    # 'Cookie': '_gaexp=GAX1.2.nr2c3GE4S7yNtDc8v1RXpg.19349.1!RT-H9pSzT_SrFt4W13rv7g.19393.1!wnRXqZWOSEqho9JMFw_FvA.19403.1!PeTJGbW1QZSlhSATi8Xbtw.19428.1!ixTmMHm5Qf6wJvC0cRUkqQ.19364.0; V=201; _gcl_au=1.1.963077808.1671189846; sessionStatus=true|undefined; FirstPage=Fri Dec 16 2022 16:54:48 GMT+0530 (India Standard Time); AB=B; _ga=GA1.2.2009134722.1671189846; _gid=GA1.2.1532272683.1671189846; _fbp=fb.1.1671189846479.835917552; _fpuuid=Qusczw-1F8PHB7H-Cxi2k; ImpressionCookie=0; cdigiMrkt=utm_source%3A%7Cutm_medium%3A%7Cdevice%3Ad%7Cexpires%3ASun%2C%2015%20Jan%202023%2011%3A24%3A48%20GMT%7C; _dc_gtm_UA-68002030-1=1',
}

params = {
    'fields': 'SITE',
    'currentPage': '2',
    'pageSize': '45',
    'format': 'json',
    'query': ':relevance',
    'sortBy': 'relevance',
    'curated': 'true',
    'curatedid': 'boys-denims-trousers',
    'gridColumns': '3',
    'facets': '',
    'advfilter': 'true',
    'platform': 'Desktop',
    'showAdsOnNextPage': 'false',
    'is_ads_enable_plp': 'false',
}

response = requests.get('https://www.ajio.com/api/category/83', params=params, headers=headers)
# print(response.json())

js=response.json()
l=[]
product=js['products']
for i in product:
    pro_url="https://www.ajio.com"+i.get('url')
    code=i.get('code')
    # print(pro_url)
    image= js['products'][0]['images']
    im =[]
    for p in image:
        imgs = p.get('url')
        im.append(imgs)
        # print(imgs)
    price=i.get('price').get('displayformattedValue')
    offer_price=i.get('offerPrice')
    dis_per=i.get('discountPercent')
    data={
        'pro_url' : pro_url,
        'code' : code,
        'image' : im,
        'price' : price,
        'offer_price' : offer_price,
        'dis_per' : dis_per
    }
    
    l.append(data)
    print(l)
    # print(image)
    
    df=pd.DataFrame(l)
    df.to_excel("ajio1.xlsx",index=False)