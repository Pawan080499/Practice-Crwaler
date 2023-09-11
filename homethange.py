import re
# from mysqlx import Row
import csv
import requests
from requests import Session
#import mysql.connector

s =  Session()
s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"
from bs4 import BeautifulSoup as bs
from lxml import html
import pandas as pd

# conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'root', db = 'company')
# cursor = conn.cursor()

f = open("homethangs_detail_pge.csv","w",encoding="utf-8",newline="")
csv_file = csv.writer(f)
csv_file.writerow(["Links","Title","Price","Retail_price","UPC","MPN","Width","Length","Hieght","Metarial","Image"])

all_links = []

def misc_links (link):
    r = s.get(link)
    tree = html.fromstring(r.text)
    soup = bs(r.content,"html.parser")
    read=open("homethangs_output_file.xlsx","r").read().split("\n")
    product_name= "".join(tree.xpath("//div[@class='tpbbgg']//text()")[3].replace('\n',''))
    price= "".join(tree.xpath("//span[@class='price']//text()")[0])
    retail_price="".join(tree.xpath("//span[@class='panaa rgpr']//text()")).strip().replace("Retail Price:","").replace("\xa0 ","")
    upc="".join(tree.xpath("//td[@class='item-info']//text()")[14].strip())
    mpn="".join(tree.xpath("//td[@class='item-info']//text()")[15].strip())
    width="".join(tree.xpath("//td[@class='item-info']//text()")[16].strip())
    lenght="".join(tree.xpath("//td[@class='item-info']//text()")[17].strip())
    height="".join(tree.xpath("//td[@class='item-info']//text()")[18].strip())
    material="".join(tree.xpath("//td[@class='item-info']//text()")[20].strip())
    image="".join(tree.xpath("//td[@class='bigimage mapan']//p//img//@src"))
    csv_file.writerow([link,product_name,price,image])
    # query = 'insert into homethange(link, product_name,price,image) values(%s,%s,%s,%s)'
    # values = [link,product_name,price,image]
    # cursor.execute(query,values)
    # conn.commit()

    print(link)

def all_product_link(link):
    r = s.get(link)
    tree = html.fromstring(r.text)
    soup = bs(r.content,"html.parser")
    links=tree.xpath("//td[@class='cat-item-name']//a//@href") 
    for i in links(1,70):
        m_links = "https://www.homethangs.com"+''.join(links).strip()
        print(m_links)
        all_links.append({"links:m_links"})


def list_page(link):
    r = s.get(link)
    tree = html.fromstring(r.text)
    soup = bs(r.content,"html.parser")
    products = tree.xpath("//table[@class='categoryitem']")
    for product in products:
        prod_url = product.xpath(".//td[@class='cat-item-name']//a//@href")
        m_url = "https://www.homethangs.com/"+''.join(prod_url).strip()
        print(m_url)
        all_links.append({"Links":m_url})


def crawling_subcategory(link):
    r = s.get(link)
    tree = html.fromstring(r.text)
    soup = bs(r.content,"html.parser")
    sub_links = tree.xpath("//div[@class='category-list']//p//a//@href")
    for sb_links in sub_links:
        m_url = "https://www.homethangs.com/"+sb_links
        list_page(m_url)


# cat_links = open("homethange.csv").read().split("\n")
# for c_link in cat_links:
#     crawling_subcategory(c_link)


# df = pd.DataFrame(all_links)
# df.to_excel("homethangs_output_file.xlsx",index=False)


df = pd.read_excel("homethangs_outputtt_file.xlsx")
links = df["Links"].to_list()
for link in links:
    misc_links(link)




# url= "https://www.homethangs.com/"
# f=open("homethange.csv","w",encoding="utf-8")
# r=requests.get(url)
# soup=bs(r.content,("html.parser"))
# products=soup.find_all("ul","dropdown")
# for i in products:
#     e=i.find("li").find("a").get("href")
#     print(i)
#     f.write("https://www.homethangs.com"+e+"\n")


