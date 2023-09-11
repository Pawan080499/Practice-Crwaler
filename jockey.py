import requests
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.jockey.in/',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiIxZDg1OTVhNy1lNThiLTRkM2YtODY2NC1jOWFiOTNmYjA2ZWMiLCJhaWQiOiJDQUQ1MDU5MC1BMTg5LTQxNEYtQTJGNS0xMDMzOUQxRjlGOTciLCJkaWQiOiI0NDQ5NkIwMy0zNjQ3LTQ5MEMtQjJGMC0yRTE1OUIyN0QyNzgiLCJuYmYiOjE2ODY1NzEwMDAsImV4cCI6MTY4NjY1NzQwMCwiaWF0IjoxNjg2NTcxMDAwfQ.9PzFVO0uJZ4oZQ08LSIMFkIvDhYgChdyVeO0xS_G8qM',
    'Origin': 'https://www.jockey.in',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
}

params = {
    'cat1': 'men',
    'cat2': '',
    'cat3': '',
    'cat4': '',
    'ps': '12',
    'by': '',
    'ctkn': '',
    'dir': '',
    'f': '',
    'ifr': '0',
}
l =[]

for i in range(1,26):
    params['pno']=str(i)
    
    response = requests.get('https://api.jockey.in/api/productsbystylesV1', params=params, headers=headers)


    js=response.json()
    products=js['Data']['StyleDetails']

    for product in products:
        pro_url="https://www.jockey.in/"+product.get('ProductURL')
        MinimumPrice=product.get('MinimumPrice')
        AvailableSizes=product.get('AvailableSizes')
        ProductTitle=product.get('ProductTitle')
        color=product.get('ColorName') 
        data={
            'url' : pro_url,
            'Price' : MinimumPrice,
            'Sizes':AvailableSizes,
            'title' : ProductTitle,
            'color' : color,
            
        }
        l.append(data)
    print(response.url)
    
df = pd.DataFrame(l)
df.to_excel("jockey.xlsx",index=False)