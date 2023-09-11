import requests
import pandas as pd

l=[]
def crawl():
    # https://www.shiksha.com/engineering/colleges/b-tech-colleges-india-4?rf=searchWidget&landing=ctp
    has_next = True
    hash = 'eyJyZiI6InNlYXJjaFdpZGdldCIsImxhbmRpbmciOiJjdHAiLCJ1cmwiOiIvZW5naW5lZXJpbmcvY29sbGVnZXMvYi10ZWNoLWNvbGxlZ2VzLWluZGlhIiwiZnIiOiJ0cnVlIiwiZmV0Y2hQQ1ciOnRydWV9'
    while has_next:
        cookies = {
            'visitorId': 'b830e931675081967v400v641159472',
            'visitorSessionId': 'b830e931675081967v400v641159472s479056747',
            'countryId': 'IN',
            'ak_bmsc': '0B31456FA0B42664A99013470B400E40~000000000000000000000000000000~YAAQbRwgFyD3VNCFAQAACGuqAhKFlThl3iZInRnkXzKGlQHLJNubFpr7oukrRzUW3Jv5poYCjF3611vEEeR9WjZGglp294CR/4Hz5pfQkcoZHHGdv5p+BhSsii7uCajWOJx+EH731jGA+M+vWSdGoMcRvtsIKJUMBr8NY4NBVTQeDRBYfpCwW2kFr8h+uUsqgGjYjHlGiJxqieE4reVCr7Pbg8XW9Wxjm46hYLpoqcOgFUkRKoK5Y2sfAKufa6yUaJ0Sz6/ixYMLdQ5npbxC/1JJwiFmXGwG/HJDX7iI40Mf8T7HoxAw8OBZwn1h2oz6n2C6XYaP5UbWfZoRz2CYTp63s26t27Tfq5J4xFJuHOs4kI/KEDbaihVlpbZa5E6jGW7VmbrCNnHLpvy31kEvx5Nv5wDJPBWIzutDQBBbufTq5Nj1plHY2/9GuvJVeFNu45QK/BnlyBRlgaqxI3wH3gjLItuMV6bSUj2gK1qmobTzQhy1xW1OhqWLbpEAwQ==',
            'hpTab': 'mba',
            'ispwa': 'true',
            'SAinit': '1',
            'bm_sv': 'A72AFA167BA66E5BA755FF6ACC6BF37C~YAAQbRwgF8n3VNCFAQAAVWGrAhINL3409gU0rQe8AGrNgq8OR1jMX5kG2xpcu/p21Aqn2blyzCdT9e0FH6vKTntlTNFrenf9LLhmBZRls+9FVWne2XucmHDSZqR/xIcmoghKZr1LZaaN9eU2sqsYU1B4WRvC0Gm8vI+m3dJxHkvZO91NUYYud4E+BLSmQqsXXk6Wi4om4cgaRjuqWzbWEU2eQVbBDSIc/h0SsR6981acP4RELP7uttfLUBUYMqPGXuM=~1',
            'tracker': '1675081968rzcEeLSmF4rn9OfKf',
            'lastVisitTime': '1675082016',
            'siteview': 'desktop',
            '_ga': 'GA1.2.2057312935.1675081968',
            '_gid': 'GA1.2.1757243928.1675081968',
            '__gads': 'ID=0722df7dd6d61266:T=1675081969:S=ALNI_MYzpYLnJtB7GUIoMLWs3NrzOWtRig',
            '__gpi': 'UID=00000bb15dee5d29:T=1675081969:RT=1675081969:S=ALNI_MYGH8Cgj8mysJAv2YCk9W1BDyNpfQ',
            '_clck': 'mukc62^|1^|f8p^|0',
            '_fbp': 'fb.1.1675081969943.490477630',
            '_clsk': 'r9neuf^|1675082030894^|7^|0^|j.clarity.ms/collect',
            'recentSearches': 'W3sidHVwbGVEYXRhIjp7ImlkIjoxMCwibmFtZSI6IkIuRS4gLyBCLlRlY2giLCJ0eXBlIjoiYmFzZV9jb3Vyc2UiLCJzdWJUeXBlIjpudWxsLCJ1cmwiOiIvYi10ZWNoL2NvbGxlZ2VzL2ItdGVjaC1jb2xsZWdlcy1pbmRpYT9yZj1zZWFyY2hXaWRnZXQmbGFuZGluZz1jdHAiLCJxdWVzdGlvbkNvdW50IjowLCJhbnN3ZXJDb3VudCI6MCwibXVsdGlwbGUiOmZhbHNlfSwiYnVja2V0IjoiQ29sbGVnZXMifV0^%^3D',
            'ctpgRandom': '4847',
            'gdpr': '1675082016',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Origin': 'https://www.shiksha.com',
            'Connection': 'keep-alive',
            'Referer': 'https://www.shiksha.com/',
            # 'Cookie': 'visitorId=b830e931675081967v400v641159472; visitorSessionId=b830e931675081967v400v641159472s479056747; countryId=IN; ak_bmsc=0B31456FA0B42664A99013470B400E40~000000000000000000000000000000~YAAQbRwgFyD3VNCFAQAACGuqAhKFlThl3iZInRnkXzKGlQHLJNubFpr7oukrRzUW3Jv5poYCjF3611vEEeR9WjZGglp294CR/4Hz5pfQkcoZHHGdv5p+BhSsii7uCajWOJx+EH731jGA+M+vWSdGoMcRvtsIKJUMBr8NY4NBVTQeDRBYfpCwW2kFr8h+uUsqgGjYjHlGiJxqieE4reVCr7Pbg8XW9Wxjm46hYLpoqcOgFUkRKoK5Y2sfAKufa6yUaJ0Sz6/ixYMLdQ5npbxC/1JJwiFmXGwG/HJDX7iI40Mf8T7HoxAw8OBZwn1h2oz6n2C6XYaP5UbWfZoRz2CYTp63s26t27Tfq5J4xFJuHOs4kI/KEDbaihVlpbZa5E6jGW7VmbrCNnHLpvy31kEvx5Nv5wDJPBWIzutDQBBbufTq5Nj1plHY2/9GuvJVeFNu45QK/BnlyBRlgaqxI3wH3gjLItuMV6bSUj2gK1qmobTzQhy1xW1OhqWLbpEAwQ==; hpTab=mba; ispwa=true; SAinit=1; bm_sv=A72AFA167BA66E5BA755FF6ACC6BF37C~YAAQbRwgF8n3VNCFAQAAVWGrAhINL3409gU0rQe8AGrNgq8OR1jMX5kG2xpcu/p21Aqn2blyzCdT9e0FH6vKTntlTNFrenf9LLhmBZRls+9FVWne2XucmHDSZqR/xIcmoghKZr1LZaaN9eU2sqsYU1B4WRvC0Gm8vI+m3dJxHkvZO91NUYYud4E+BLSmQqsXXk6Wi4om4cgaRjuqWzbWEU2eQVbBDSIc/h0SsR6981acP4RELP7uttfLUBUYMqPGXuM=~1; tracker=1675081968rzcEeLSmF4rn9OfKf; lastVisitTime=1675082016; siteview=desktop; _ga=GA1.2.2057312935.1675081968; _gid=GA1.2.1757243928.1675081968; __gads=ID=0722df7dd6d61266:T=1675081969:S=ALNI_MYzpYLnJtB7GUIoMLWs3NrzOWtRig; __gpi=UID=00000bb15dee5d29:T=1675081969:RT=1675081969:S=ALNI_MYGH8Cgj8mysJAv2YCk9W1BDyNpfQ; _clck=mukc62^|1^|f8p^|0; _fbp=fb.1.1675081969943.490477630; _clsk=r9neuf^|1675082030894^|7^|0^|j.clarity.ms/collect; recentSearches=W3sidHVwbGVEYXRhIjp7ImlkIjoxMCwibmFtZSI6IkIuRS4gLyBCLlRlY2giLCJ0eXBlIjoiYmFzZV9jb3Vyc2UiLCJzdWJUeXBlIjpudWxsLCJ1cmwiOiIvYi10ZWNoL2NvbGxlZ2VzL2ItdGVjaC1jb2xsZWdlcy1pbmRpYT9yZj1zZWFyY2hXaWRnZXQmbGFuZGluZz1jdHAiLCJxdWVzdGlvbkNvdW50IjowLCJhbnN3ZXJDb3VudCI6MCwibXVsdGlwbGUiOmZhbHNlfSwiYnVja2V0IjoiQ29sbGVnZXMifV0^%^3D; ctpgRandom=4847; gdpr=1675082016; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

        params = {
            'data': hash,
        }

        response = requests.get(
            'https://apis.shiksha.com/apigateway/categorypageapi/v2/info/getCategoryPageFull',
            params=params,
            cookies=cookies,
            headers=headers,
        )
        

        js = response.json()
        
        pro = js['data']['instituteTuples']

        for i in pro:
            name = i.get('name')
            url = "https://www.shiksha.com"+i.get('url')
            rating = i.get('rating')
            
            data = {
                'name':name,
                'url':url,
                'rating':rating
            }
            
            # l.append(data)
            print(data)
            if js['data']['paginationData']['nextUrls']:
                # if js['data'].get('categoryUrlHash'):
                hash = js['data'].get('categoryUrlHash')
            else:
                has_next = False
                
crawl()        
      
df=pd.DataFrame(l)
df.to_excel("shiksha.csv",index=False)
