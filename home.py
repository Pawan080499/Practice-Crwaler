from requests import Session
s = Session()
from bs4 import BeautifulSoup as bs
from lxml import html
l=[]

base_url = "https://www.homethangs.com{}"
def header_link(url):
    r=s.get(url)
    # soup=bs(r.text,"html.parser")
    tree = html.fromstring(r.text)
    link = tree.xpath("//div[@class='nav-column']//a")
    for i in link:
        e=i.get('href')
        url = "https://www.homethangs.com/{}".format(e)
        sub_link(e)  

        # #  print(len("https://www.homethangs.com/"+e))
        # print("https://www.homethangs.com/"+e)         
        # url="https://www.homethangs.com/"

def sub_link(url):
    r=s.get(url)
    tree = html.fromstring(r.text)
    soup=bs(r.content,"html.parser")
    product = soup.find_all("td","cat-item-name")
    if product:
        list_page(url)
    for i in tree.xpath("//div[@class='category-list']"):
        b=i.find('a').get('href')
        print("https://www.homethangs.com/"+b)

        sub_link(b)
        
def list_page(url):
    r=s.get(url)
    soup=bs(r.text,"html.parser")
    links = soup.find_all("td","cat-item-name")
    for i in links:
        d=i.find('a').get('href')
        title = soup.find("td","cat-item-name").text.strip()
        sale_price = soup.find("td","before-price").find_all('span')[3].text
        img = soup.find("table","categoryitem").find('a').find('img').get('src')
        data={
            "title":title,
            "price":sale_price,
            'image':img,
        } 
        l.append(data)
        print(l)
#         # print(len("https://www.homethangs.com/"+d))
# # url="https://www.homethangs.com/decorative-figurines-799.html"    


# header_link("https://www.homethangs.com/")





# links =[]
# for i in tree.xpath('//div[@id="menu-wrapper"]//ul//li//a/@href'):
#     if  '/blog/' not in i:
#         if '#' not in i:
#             links.append("https://www.homethangs.com"+i)

# tree.xpath('//div[@id="menu-wrapper"]//ul//li//ul[not (contains(@class, "dropdown"))]//a/@href')