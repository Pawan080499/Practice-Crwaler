from requests import Session
s = Session()
from bs4 import BeautifulSoup as bs
import pandas as pd

# f = open("india.csv","w",encoding="utf-8")
l=[]
list_page_ = []
def crawl_sub_cat(url):
    r=s.get(url)
    soup = bs(r.content,("html.parser"))
    sub_links=soup.find_all('div','boxN trck')
    for i in sub_links:
        sub_cat={}
        e='https://dir.indiamart.com'+i.find('a').get('href') 
        # d=('https://dir.indiamart.com/'+e)    
        sub_cat={
            "url":e
        }
        print(sub_cat)
        l.append(sub_cat)

def list_page(row):
    url =row['url']
    r=s.get(url)
    soup = bs(r.content,("html.parser"))
    links=soup.find_all("div","rht pnt flx")
    for i in links:
        dic={}
        title=i.find('span',"pnm ldf cur")
        if title:
            title = title.text
        else:
            title = "Not given"
        img=i.find('div','prd-img')
        if img:
            img_url = img.find("img").get("src")
        else:
            img_url = "Not given"
        spc=soup.find('div','desc des_p elps3l')
        specification= ""
        if spc:
            for i in spc.find_all('p'):
                specification += i.text
        else:
            specification="Not given"        
        dic={
            "title":title,
            "image":img_url,
            "specificaiton":specification
        }
        print(dic)
        list_page_.append(dic)
        
        
url="https://dir.indiamart.com/indianexporters/plywood.html"
crawl_sub_cat(url)

# df = pd.DataFrame(l)
# df.to_excel("india.xlsx",index=False)

# df=pd.read_excel("india.xlxs")
for i in l:
    list_page(i)

df=pd.DataFrame(list_page_)
df.to_excel("india_list_page.xlsx",index=False)
        
    
        