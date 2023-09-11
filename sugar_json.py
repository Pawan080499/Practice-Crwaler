import requests
from requests import Session
s = Session()
from bs4 import BeautifulSoup as bs
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Origin': 'https://in.sugarcosmetics.com',
    'Connection': 'keep-alive',
    'Referer': 'https://in.sugarcosmetics.com/', 
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

json_data = {
    'collection_handle': 'makeup',
    'sort': 'relevance',
    'filter': {},
    'skip': 40,
    'count': 20,
    'device_id': '3c77-2427-41fe-af1f-8cdd8d7e345a',
}

response = requests.post('https://prod.api.sugarcosmetics.com/collections/prod/getCollectionv2', headers=headers, json=json_data)

# print(response.json())
js=response.json()
l=[]
product=js['resbody']['result']
for i in product:
    pro_url="https://in.sugarcosmetics.com/products/"+i.get('handle')
    id=i.get('id')
    pro_price=i.get('product_price')
    # print(pro_price)
    ave_rating=i.get('averageRating')
    ave_count=i.get('rating_count')
    
    data={
        'pro_url' : pro_url,
        'id' : id,
        'pro_price': pro_price,
        'ave_rating' : ave_rating,
        'ave_count' : ave_count,
        
    }
    
    l.append(data)
    print(l)
    
    
    
df = pd.DataFrame(l)
df.to_excel("sugar.xlsx",index=False)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # curl to python
    #  js = response.json()
    #  js.keys()
    # #  dict_keys(['statusId', 'message', 'resbody'])      //check result thand find one by object
    # js['resbody']                       //show all product details
    # js['resbody'].keys()                 //next show all product details
    # dict_keys(['result', 'bannerImages', 'stickyText', 'bulk_buy', 'collection', 'textFacets', 'selectedtextFacets', 'total_count'])
    # js['resbody']['result']               // show all details like id,title,name
    # js['resbody']['result'][0].keys()
    # js['resbody']['result'][0]['collection_handle']      // take one by one like id,title,name,
    # js['resbody']['result'][1]['product_price']
    # js['resbody']['result'][1]['averageRating']
    
    
    
    
    # for i in js['products']:
    #      print(i['landingPageUrl'])     for all links
    
    # s = requests.session()
# r = s.get(url,verify = False)    when response not response


# js['hits'][0]['url'] + '/' + js['hits'][0]['plp_product_group_code'] + '/p/'
 
    
    
                            # soup.find_all('div','boxN trck').__len__()
                            # [i.find('a').get('href') for i in soup.find_all('div','boxN trck')]

                            # for i in soup.find_all('div','boxN trck'):
                            #      e=i.find('a').get('href')
                            #     print('https:/dir.indiamart.com'+e)
    



# https://dir.indiamart.com/impcat/shuttering-plywood.html


# detail=[]
# 
# set(tree.xpath("//div[@id='cat-tiles-content']//a/@href")).__len__()
# set remove duplicate




# info = {}
# info = dict(zip(headings,values))


# https://legacy.reactjs.org/docs/getting-started.html    react js