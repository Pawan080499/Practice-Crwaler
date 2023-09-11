from requests import Session
s = Session()
from bs4 import BeautifulSoup as bs
from lxml import html
import pandas as pd

l=[]


def pdp_page(data_dict):
    print(data_dict)
    pdp_url = "https:{}".format(data_dict.get("list_link"))
    r = s.get(pdp_url)
    soup=bs(r.content,"html.parser")
    price=soup.find('span','h3 font-weight-bold mb-1 text-nowrap sale-price').text
    title=soup.find('div','mb-4 d-flex align-items-center flex-wrap').text
    headings=[i.text for i in soup.find_all('h2','h5 font-weight-bold mb-0 mr-3 module-title d-inline-block')]
    values=[i.find('div',attrs={'aria-pressed':'true'}).text for i in soup.find_all('div','d-flex flex-wrap options')]
    info={}
    info=dict(zip(headings,values))
    print(price,info,title)
    
    
def sub_link(url):
    r=s.get(url)
    tree = html.fromstring(r.text)
    link=tree.xpath("//div[@class='cat-fran-card-text']//h2//a/@href")
    # for i in sub_link:
    #     if 'https://www.dell.com/en' in i:
    #         link = i
    #     print(link)
    for i in link:
        if 'https:' not in i:
            link = 'https:' + i
        else:
            link = i
        data={
            "link":link,
        }
        print(data)
        l.append(data)
     
def list_page(row):
    cat_url = row.get("link")
    r=s.get(cat_url)
    # tree=html.fromstring(r.text)
    soup=bs(r.content,"html.parser")
    listpage=soup.find_all('h3','ps-title')
    for i in listpage:
        e=i.find('a').get('href')
        # print('https:'+i)
        data={
            "cat_url": cat_url,
            'list_link':e,
        }
        
        # records.append(data)
        pdp_page(data)
    
        
           
# this is for Subcategories/Sublinks     
url="https://www.dell.com/en-in/shop/scc/sc/laptops"
sub_link(url)
records = []

# This is for List page functions
for cat_link in l:
    list_page(cat_link)


# This is for PDP urls
# for pdp_url in records:
#     pdp_page(pdp_url)

    
    


df = pd.DataFrame(l)
df.to_excel("dell.xlsx",index=False)

df = pd.DataFrame(records)
df.to_excel("dell_listpage.xlsx",index=False)


