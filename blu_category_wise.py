from requests import Session
s = Session()
from bs4 import BeautifulSoup as bs
import pandas as pd
url="https://bluebungalow.com.au/collections/womens-clothing"
l=[]
def list_page(url):
    response=s.get(url)
    soup=bs(response.text,"html.parser")
    link=soup.find_all('div','results-grid__tile')
    for i in link:
        e="https://bluebungalow.com.au"+i.find('a').get('href')
        print(e)
        data={
            "link":e,
        }
        l.append(data)
        # print(l)

listpage = []
for page in range(1,34):
    url = f"https://bluebungalow.com.au/collections/womens-clothing?page={page}"
    list_page(url)
    print(page)


        
        
# list_page(url)

df=pd.DataFrame(l)
df.to_excel("blue.xlsx",index=False)
