from requests import Session
s = Session()
from bs4 import BeautifulSoup as bs
import pandas as pd
url="https://bluebungalow.com.au/collections/womens-clothing"
l=[]
listpage=[]
def main_page(url):
    r=s.get(url)
    soup=bs(r.content,"html.parser")
    link=soup.find('div','main-navigation').find('ul').find_all('li')
    for i in link:
        e=i.find('a').get('href')
        if "https://bluebungalow.com.au" in e:
            # print(e)
            l.append(e)
main_page(url)

# for page in range(1,10):
#     url = f"https://bluebungalow.com.au/collections/shoes?page={page}"
    
#     list_page(url)
#     print(page)
    
def list_page(url):
    r=s.get(url)
    soup=bs(r.text,"html.parser")
    product=soup.find_all('div','results-grid__tile')
    for i in product:
        link=i.find('a').get('href')
        links="https://bluebungalow.com.au"+link
        title=i.find('h4','product-card__title text--regular text--small-max-md')
        if title:
            title = title.text.split()
        else:
            title = "none"
            
        price=i.find('span','money')
        if price:
            price = price.text
        else:
            price = "none"
        data={
            "links":links,
            "title":title,
            "price":price,
        }
        # print(data)
        # listpage.append(data)

def product_page(url):
    r=s.get(url)
    soup=bs(r.text,"html.parser")
    title=soup.find("div","product-name top-product-detail").text.split()
    price=soup.find('span','money').text
    review=soup.find('div','oke-sr-count').text
    rating=soup.find('span','oke-w-ratingAverageModule-rating-average').text
        
    


# pd=pd.DataFrame(l)
# pd.to_excel("newblue.xlsx",index=False)