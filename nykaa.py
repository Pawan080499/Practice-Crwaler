from requests import Session
s = Session()
from bs4 import BeautifulSoup as bs
import pandas as pd
s.headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
s = Session()
l=[]
for i in range(1,10):
    url="https://www.nykaa.com/nykaa-cosmetics-moi-range/c/24631?page_no=2&sort=popularity&transaction_id=cd431e1c57e6e73913acc7b4eba822f1&intcmp=nykaa:hp:desktop-homepage:default:top_brands:COLUMN_GRID:5:Nykaa%20Cosmetics:cd431e1c57e6e73913acc7b4eba822f1&eq=desktop".format(i)
    r = s.get(url.format(i))
    soup = bs(r.content,"html.parser")
    links=soup.find_all("div","css-fn0ggt")
    for link in links:
         e=link.find('a').get('href')
         print(e)
         l.append({"links":"https://www.nykaa.com"+e})
        #  print(response.status_code)
    # print(i, '...............')
    
    df=pd.DataFrame(l)
    df.to_excel("nykaa.xlsx",index=False)

  
