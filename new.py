from requests import Session
s = Session()
from bs4 import BeautifulSoup as bs


cookies = {
    'T': 'TI168631844793400058745206955744114100876675609296441838366071797069',
    'SN': 'VIC566CAA4F0884A009317B03A48D367F1.TOKF03F0C5CE24B4DAA9B3DC5E1B3586341.1686318451.LO',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE2ODgwNDY0NTEsImlhdCI6MTY4NjMxODQ1MSwiaXNzIjoia2V2bGFyIiwianRpIjoiNGVjMDEyNjEtY2EzOC00NGVlLWJiZDItNTgwYTUwZGNjNWIyIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjg2MzE4NDQ3OTM0MDAwNTg3NDUyMDY5NTU3NDQxMTQxMDA4NzY2NzU2MDkyOTY0NDE4MzgzNjYwNzE3OTcwNjkiLCJrZXZJZCI6IlZJQzU2NkNBQTRGMDg4NEEwMDkzMTdCMDNBNDhEMzY3RjEiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.j1oXDZjfe8lmJQ_TM3sRDavhdlqDQQOUXs1GIPFEH_4',
    'K-ACTION': 'null',
    'AMCV_17EB401053DAF4840A490D4C^%^40AdobeOrg': '-227196251^%^7CMCIDTS^%^7C19518^%^7CMCMID^%^7C84335686871169475502224007284755579032^%^7CMCAAMLH-1686923249^%^7C12^%^7CMCAAMB-1686923249^%^7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y^%^7CMCOPTOUT-1686325649s^%^7CNONE^%^7CMCAID^%^7CNONE',
    'AMCVS_17EB401053DAF4840A490D4C^%^40AdobeOrg': '1',
    'pxcts': '2dc72c9c-06cc-11ee-ae54-5376736d7042',
    '_pxvid': '2dc72118-06cc-11ee-ae54-c334c61b9e34',
    '__pxvid': '2e512cca-06cc-11ee-8c4e-0242ac120002',
    'S': 'd1t18Pz8/P3s/N24TcD8vVz8/PyE7uxgb2H49x88iGJJnacnbcVcdXB2rZqaoZqgZItT/bNSgjTI8D0DA81IxD5Ug3g==',
    '_px3': '70e92f06f53ab8bc244d1242cf4a41f5f1929442f39d9b70f5b0d8c328ee2760:xEE1rFZQi7g8gB19Tk4L7Ih7vxFAiJ/GjCAOsU2bUvCa8dp6vdnb8rrg1S7qjdM93djHppVJ13+ZLdDMvYfraw==:1000:mM4aO3VFiqlLOwpsfvecd8tqhNHUwPmNKqNS3cxlyuA/lxQHsTkCOiyHxhtCKzAz0wrFaG35t5xqvLm8RodoBC3oUvvxHBA9/Y+zTpVY+x72VZ2GEe4c3hkL/U/iq0D+PbQpkXZGV9N29IWxx7vnyRq/wA6JXVpAVU7xOV49HVtkJJk8GD0oBiv5VZSXCSe8kZ5Rfl1S9iWJq6oS7K7ARw==',
    's_sq': 'flipkart-prd^%^3D^%^2526pid^%^253Dwww.flipkart.com^%^25253A^%^2526pidt^%^253D1^%^2526oid^%^253Dhttps^%^25253A^%^25252F^%^25252Fwww.flipkart.com^%^25252Fmobiles^%^25252Fpr^%^25253Fsid^%^25253Dtyy^%^2525252C4io^%^252526p^%^2525255B^%^2525255D^%^25253Dfacets.availability^%^252525255B^%^252525255D^%^2525253DExclude^%^2525252B^%^2526ot^%^253DA',
    'qH': 'd2974c96dc96b3f3',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Connection': 'keep-alive',
    # 'Cookie': 'T=TI168631844793400058745206955744114100876675609296441838366071797069; SN=VIC566CAA4F0884A009317B03A48D367F1.TOKF03F0C5CE24B4DAA9B3DC5E1B3586341.1686318451.LO; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE2ODgwNDY0NTEsImlhdCI6MTY4NjMxODQ1MSwiaXNzIjoia2V2bGFyIiwianRpIjoiNGVjMDEyNjEtY2EzOC00NGVlLWJiZDItNTgwYTUwZGNjNWIyIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjg2MzE4NDQ3OTM0MDAwNTg3NDUyMDY5NTU3NDQxMTQxMDA4NzY2NzU2MDkyOTY0NDE4MzgzNjYwNzE3OTcwNjkiLCJrZXZJZCI6IlZJQzU2NkNBQTRGMDg4NEEwMDkzMTdCMDNBNDhEMzY3RjEiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.j1oXDZjfe8lmJQ_TM3sRDavhdlqDQQOUXs1GIPFEH_4; K-ACTION=null; AMCV_17EB401053DAF4840A490D4C^%^40AdobeOrg=-227196251^%^7CMCIDTS^%^7C19518^%^7CMCMID^%^7C84335686871169475502224007284755579032^%^7CMCAAMLH-1686923249^%^7C12^%^7CMCAAMB-1686923249^%^7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y^%^7CMCOPTOUT-1686325649s^%^7CNONE^%^7CMCAID^%^7CNONE; AMCVS_17EB401053DAF4840A490D4C^%^40AdobeOrg=1; pxcts=2dc72c9c-06cc-11ee-ae54-5376736d7042; _pxvid=2dc72118-06cc-11ee-ae54-c334c61b9e34; __pxvid=2e512cca-06cc-11ee-8c4e-0242ac120002; S=d1t18Pz8/P3s/N24TcD8vVz8/PyE7uxgb2H49x88iGJJnacnbcVcdXB2rZqaoZqgZItT/bNSgjTI8D0DA81IxD5Ug3g==; _px3=70e92f06f53ab8bc244d1242cf4a41f5f1929442f39d9b70f5b0d8c328ee2760:xEE1rFZQi7g8gB19Tk4L7Ih7vxFAiJ/GjCAOsU2bUvCa8dp6vdnb8rrg1S7qjdM93djHppVJ13+ZLdDMvYfraw==:1000:mM4aO3VFiqlLOwpsfvecd8tqhNHUwPmNKqNS3cxlyuA/lxQHsTkCOiyHxhtCKzAz0wrFaG35t5xqvLm8RodoBC3oUvvxHBA9/Y+zTpVY+x72VZ2GEe4c3hkL/U/iq0D+PbQpkXZGV9N29IWxx7vnyRq/wA6JXVpAVU7xOV49HVtkJJk8GD0oBiv5VZSXCSe8kZ5Rfl1S9iWJq6oS7K7ARw==; s_sq=flipkart-prd^%^3D^%^2526pid^%^253Dwww.flipkart.com^%^25253A^%^2526pidt^%^253D1^%^2526oid^%^253Dhttps^%^25253A^%^25252F^%^25252Fwww.flipkart.com^%^25252Fmobiles^%^25252Fpr^%^25253Fsid^%^25253Dtyy^%^2525252C4io^%^252526p^%^2525255B^%^2525255D^%^25253Dfacets.availability^%^252525255B^%^252525255D^%^2525253DExclude^%^2525252B^%^2526ot^%^253DA; qH=d2974c96dc96b3f3',
}

url="https://www.flipkart.com/search?q=watch&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

def getdata(url):
    r = s.get(url,headers=headers,cookies=cookies)
    soup=bs(r.text,"html.parser")
    return soup


def paggination(soup):
    page=soup.find("div","_2MImiq")
    if not page.find("a","ge-49M"):
        url = "https://www.flipkart.com"+ str(page.find("a","_1LKTO3"))
        return url
    else:
        return


# while True:
    
soup = getdata(url)
url=paggination(soup)
# if not url:
#     break
print(url)

# print(getdata(url))

