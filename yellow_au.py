from requests import Session
s = Session()
import math
from bs4 import BeautifulSoup as bs
import pandas as pd
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.yellowpages.com.au/',
    'Connection': 'keep-alive',
    # 'Cookie': 'ak_bmsc=A532D29B897162F75A751DD1BCB7515F~000000000000000000000000000000~YAAQTHxBFx8A/nyIAQAAkXIBgRMfLAyXyiKobIUSoOC0U77CqUq6aFBPlkvoYkG4stH/7zvWaOHOdLGADUmcYrbe+J2Yrz6QFXtK/FE5yOsclpBEczugO4T242AiVKQxzJDRwl7yTU61t4ACYEQSXUv7299n19pvpFJmnIPiwCGtWfthqGgb9OraHuPcC0826T74+a3GikjL2zk+xc8AP1ViZETZQgIvvagSR9qvGpzr5/ZjVECYJkOD2DWPns3HShMLe38hn73YZoTSwZAjHTE3Ls+YssBuN6QE69AnGezkSedA29qyMO8Mn+Bz4BiKS8CsRt9MuEuiW3wFFbqZUA+Gd9xUEUaT9XC2t2gyErNeDWnGpuRCyavv4zF7JdthzCy4n2pOPhG0u4StWVpqJLrKSHP2TrNZfDrB7T+BLPxQt6mfVFcZAauyEJR/b8JGiP+GDX0MtfFukzqJZS5tzunb19QHkvTEYnCjlo+/mJ9pjLbizDg4zXZlZjINdWlNUlKco/w=; AMCV_8412403D53AC3D7E0A490D4C^%^40AdobeOrg=179643557^%^7CMCIDTS^%^7C19512^%^7CMCMID^%^7C71290915006453717283659409911720734478^%^7CMCAID^%^7CNONE^%^7CMCOPTOUT-1685798734s^%^7CNONE^%^7CMCAAMLH-1686396334^%^7C12^%^7CMCAAMB-1686396334^%^7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI^%^7CMCSYNCSOP^%^7C411-19519^%^7CvVersion^%^7C5.5.0; s_ecid=MCMID^%^7C71290915006453717283659409911720734478; AMCVS_8412403D53AC3D7E0A490D4C^%^40AdobeOrg=1; s_cc=true; RT=z=1&dm=www.yellowpages.com.au&si=95013723-0e3a-417c-8e01-6a4e9c0d20ed&ss=lifwr31v&sl=3&tt=5ov&obo=1&rl=1&ld=j8jq&r=1emw0eimx&ul=j8jr; _vwo_uuid_v2=D8FC66B2A19434E1C3BDED3F7439009FD^|dec1b7eae3da88f429f688980ac969df; _vis_opt_s=1^%^7C; _vis_opt_test_cookie=1; _vwo_uuid=D8FC66B2A19434E1C3BDED3F7439009FD; _vwo_ds=3^%^3At_0^%^2Ca_0^%^3A0^%^241685791537^%^3A54.58542661^%^3A^%^3A^%^3A3_0^%^2C2_0^%^3A0; _vwo_sn=0^%^3A4; s_sq=^%^5B^%^5BB^%^5D^%^5D; yellow-guid=9c6a26fd-9b9b-4169-ba7f-df74e690e15a; clue=lawyers solicitors; locationClue=gold coast qld; AKA_A2=A; bm_sv=6FDE98922A47D18028F542C234F009EB~YAAQTHxBF+tF/nyIAQAAAxkPgRO4UDjfFa+lIc6F5cof9iY0aJJGiKrojjUXB1JyaQGwmUA1zUFz0ZYJ9DmTUG2Y573R/1wMtixUriYmKqmNYw8xQKXIFQhaIVdavetYTNBVrYXj54KNUxANAEiY7rXvOqIjsHOfrHhml7P8Dj4OlBzGcjiA4RXqZKyw+LtDOT1JZT2ZTli1UQxEWioS17RX7L9AxRP/Wnsb4aWkHfWBpRk36+sRxY5uz6HcnDTRJWgPuVeBmNc=~1; _wingify_pc_uuid=30c5241499d7431ea052b69dcb7e1cdf; __gsas=ID=81ce04fe7d1076a3:T=1685791554:RT=1685791554:S=ALNI_MbLSIugbLR0IiN5TyFu39ahcqioYw; wingify_donot_track_actions=0; BVImplmain_site=11347; BVBRANDID=cec94ada-072c-4b90-82eb-92e082a4f4f1; BVBRANDSID=a30d3099-4936-46aa-bd38-c2bfe3badfe9',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

s.headers.update(headers)
l=[]
def main_page(url):
    r=s.get(url)
    soup=bs(r.text,"html.parser")
    link=soup.find_all('div','Box__Div-sc-dws99b-0 iOfhmk MuiPaper-root MuiCard-root PaidListing MuiPaper-elevation1 MuiPaper-rounded')
    for i in link:
        e=i.find('a').get('href')
        # title=i.find("h3","MuiTypography-root jss364 MuiTypography-h3 MuiTypography-displayBlock").text,"/",i.find("p","MuiTypography-root jss365 MuiTypography-body2 MuiTypography-colorTextSecondary").text
        landline_num=i.find("div","Box__Div-sc-dws99b-0 cZxuPV").text.replace("Call","")
        url='https://www.yellowpages.com.au/find/lawyers-solicitors/gold-coast-qld/page-{page}'
        web_side_link=soup.find_all('a','MuiButtonBase-root MuiButton-root MuiButton-text ButtonWebsite MuiButton-textSecondary MuiButton-fullWidth')
        for page in range(1,10):
            r=s.get(url.format(page))
            print(r.url)
            for c in web_side_link:
                f=c.get('href')
                data={
                "e":e,
                "web_side_link":f,
                # "title":title,
                "phone_no":landline_num,
            }
            # print("https://www.yellowpages.com.au"+e)
                    
                    
                l.append(data)
                print(data)
# main_page(l)
main_page(l)
    


df = pd.DataFrame(l)
df.to_excel("yel.xlsx",index=False)

 
