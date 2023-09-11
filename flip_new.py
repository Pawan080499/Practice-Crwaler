from requests import Session
import pandas as pd
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Connection': 'keep-alive',
    # 'Cookie': 'T=TI168491524238300072576777058316907126407532875296214788238930294191; SN=VI9D3C235F68744B498A81590C8AD71F8F.TOKF1F633B253E54C309B2DBD75A1F73E02.1684915579.LO; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE2ODY2NDMyNDksImlhdCI6MTY4NDkxNTI0OSwiaXNzIjoia2V2bGFyIiwianRpIjoiYzk1Y2I4ZWUtOGUzMS00MzgxLWExOGYtOTdiZjEzMTEyZGU3IiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjg0OTE1MjQyMzgzMDAwNzI1NzY3NzcwNTgzMTY5MDcxMjY0MDc1MzI4NzUyOTYyMTQ3ODgyMzg5MzAyOTQxOTEiLCJrZXZJZCI6IlZJOUQzQzIzNUY2ODc0NEI0OThBODE1OTBDOEFENzFGOEYiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.6Cu2xU9tqK_kUy5wvmjDHP_Zdq5SiiAj3unjsTwKlxI; K-ACTION=null; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19502%7CMCMID%7C52747548638882422692945782937159575973%7CMCAAMLH-1685520042%7C12%7CMCAAMB-1685520042%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1684922444s%7CNONE%7CMCAID%7CNONE; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; _pxvid=177c020a-fa09-11ed-8af8-70db85440004; pxcts=177c142d-fa09-11ed-8af8-525851547849; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253A%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Fclothing-and-accessories%25252Ftopwear%25252Fpr%25253Fsid%25253Dclo%25252Cash%252526p%25255B%25255D%25253Dfacets.ideal_for%252525255B%2525252%2526ot%253DA; __pxvid=1852ce37-fa09-11ed-b631-0242ac120004; S=d1t19Hj88PQw/SVoWegU/P3RIUmYN1Fs4Mooiozp6vdoLDidoc5EUv62cSgfOmNa8eVmGzivXFS62w271dl4CwYsCdg==; _px3=aa0ea3a9244f0780fbcf8a94d863ae0e6f884d4fc8fc35e6679109ec44a957c3:kqQIqPQcJ64y1Uy7eX8S8ewvbgzgU2yM1PKOpcwIoMw1sS9I8iCXTtoug1Oe0GUJOvRJG04rnQe7zvms5xHpFw==:1000:jgxDIUIGidsBTFJxqloDf4UUAHbanf8PJJ0nIWNY7Kji/PbViMm3Hfswox/BJag5SzZx7mgzQ1qHRgWA/ab0ahFuXpZviK94QqQ/FHkRF6xUYQpkCLDfM5PJ0cyhlkQ/OVcop0dw4NYQxbg0TXp6gDFGMQyZXBVOuQEb0nJIVgA8nubQvQPkHxy/B4+u5LOJBhJiM8iyUUEhClT/3ZIqqQ==',
}

s = Session()
s.headers.update(headers)
from bs4 import BeautifulSoup as bs
url="https://www.flipkart.com/clothing-and-accessories/topwear/pr?sid=clo,ash&p[]=facets.ideal_for%255B%255D%3DMen&p[]=facets.ideal_for%255B%255D%3Dmen&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_5af76f5f-e355-47dc-8af2-cad203d46365_1_372UD5BXDFYS_MC.AHHHWF67UPNB&otracker=hp_rich_navigation_1_1.navigationCard.RICH_NAVIGATION_Fashion~Men%2527s%2BTop%2BWear~All_AHHHWF67UPNB&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L2_view-all&cid=AHHHWF67UPNB"

base_url = "https://www.flipkart.com{}"

l=[]
def pdp_page(url):
    r=s.get(url)
    soup=bs(r.content,"html.parser")
    title=soup.find("span","B_NuCI")
    if title:
        title=soup.find("span","B_NuCI").text
    else:
        title="none"    
    price=soup.find("div","_30jeq3 _16Jk6d")
    if price:
        price=soup.find("div","_30jeq3 _16Jk6d").text
    else:
        price="none"
    
    review=soup.find("span","_2_R_DZ")
    if review:
        review = soup.find("span","_2_R_DZ").text
    else:
        review = "none"
    colors = []
    ul = soup.find("ul","_1q8vHb")
    if ul:
        for li in ul.find_all("li"):
            colors.append(li.find("div","_3Oikkn _3_ezix _2KarXJ _31hAvz"))
    
    if colors:
        colors = soup.find("ul","_1q8vHb").text
    else:
        colors = "none"
            
    size=soup.find('a','_1fGeJ5 _2UVyXR _31hAvz')
    if size:
        size = soup.find('a','_1fGeJ5 _2UVyXR _31hAvz').text
    else:
        size="none"
    
    image=soup.find("div","_2E1FGS _2_B7hD")
    if image:
        image = image.find('img').get('src')
    else:
        image = "Not found"
    offer=soup.find("div","_3TT44I")
    if offer:
        offer = soup.find("div","_3TT44I").text
    else:
        offer = "none"
    data={
        "Product URl":url,
        "title":title,
        "price":price,
        "review":review,
        "color":' | '.join(colors) if colors else "",
        "size":size,
        "image":image,
        "size":size,
        "offer":offer,
    }
    l.append(data)
    print(data)
    
# df = pd.DataFrame(l)
# df.to_excel("flip_new.xlsx",index=False)
    


def list_page(url):
    r=s.get(url)
    soup=bs(r.content,"html.parser")
    products = soup.findAll("div","_1xHGtK _373qXS")
    # print(product)
    for product in products:
        product_url = product.find('a')
        product_url = base_url.format(product_url.get("href")) if product_url else None
        if product_url:
            pdp_page(product_url)
            
        
            for pag in range(1,2):
                pag=[a.get("href") for a in soup.find("nav","yFHi8N").find_all("a") if "Next" in a.text]
            if pag:
                next_url = "https://www.flipkart.com{}".format(pag[0] )
                list_page(next_url)
        
url = "https://www.flipkart.com/clothing-and-accessories/topwear/pr?sid=clo,ash&p[]=facets.ideal_for%255B%255D%3DMen&p[]=facets.ideal_for%255B%255D%3Dmen&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_5af76f5f-e355-47dc-8af2-cad203d46365_1_372UD5BXDFYS_MC.AHHHWF67UPNB&otracker=hp_rich_navigation_1_1.navigationCard.RICH_NAVIGATION_Fashion~Men%2527s%2BTop%2BWear~All_AHHHWF67UPNB&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L2_view-all&cid=AHHHWF67UPNB"
list_page(url)

    
df = pd.DataFrame(l)
df.to_excel("flip_new.xlsx",index=False)

# https://www.flipkart.com/clothing-and-accessories/topwear/pr?sid=clo,ash&p[]=facets.ideal_for%255B%255D%3DMen&p[]=facets.ideal_for%255B%255D%3Dmen&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_5af76f5f-e355-47dc-8af2-cad203d46365_1_372UD5BXDFYS_MC.AHHHWF67UPNB&otracker=hp_rich_navigation_1_1.navigationCard.RICH_NAVIGATION_Fashion~Men%2527s%2BTop%2BWear~All_AHHHWF67UPNB&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L2_view-all&cid=AHHHWF67UPNB

# https://www.flipkart.com/vebnor-men-printed-casual-white-shirt/p/itm78e98d5250864?pid=SHTGJMJDYPUZRYA7&lid=LSTSHTGJMJDYPUZRYA7MMHXVV&marketplace=FLIPKART&store=clo%2Fash&srno=b_1_1&otracker=browse&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L2_view-all&fm=organic&iid=en_LKlucF0iDKZdik%2Fd%2Fn%2B5u2ybYeCtdkygcduD6fj3qiCWVEUvL2BOXdUcf3m3PXG6LCIgnZf4g4zjMZmARym%2F6A%3D%3D&ppt=browse&ppn=browse&ssid=06wbl38njwrt2eps1684920492385