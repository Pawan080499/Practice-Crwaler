import requests
import pandas as pd
from requests import Session
s = Session()

l=[]
cookies = {
    'visitor_id': '0f1c2511-86a2-4c16-95e4-0132cdf2b345',
    'RT': '"z=1&dm=noon.com&si=fbtqs13mucf&ss=ldskx8ki&sl=2&tt=2tv&rl=1&obo=1&ld=u511&r=37945691e91569bc1239898c31ce26b7&ul=u519&hd=u55j&nu=d41d8cd98f00b204e9800998ecf8427e&cl=1j2dp"',
    'nguest': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnJhV1FpT2lJeE1qUTNNR1E1WkdVeU9USTBaamt5WW1ZM1pUVTJNV001TUdZMlptSXpPQ0lzSW1saGRDSTZNVFkzTlRNME16RXpPWDAuN0kzOVpRdzR0SjVDTzhtT25HN3lDNUZhYkJkY0I0NW95ak50YTFnczB5dyIsImlhdCI6MTY3NTY3NjE1OH0.NiKin5tRnMmsJxuAZMoRnS2mowyY3LPBznPHsHTGCmA',
    '_nsc': 'nsv1.public.eyJzdGlkIjoiMmJiNzJlOGItYjk5My00NDlmLTg3OWItMmVjYmE4NGYzZjkxIiwic2lkIjoiMTI0NzBkOWRlMjkyNGY5MmJmN2U1NjFjOTBmNmZiMzgiLCJpYXQiOjE2NzU2NzYxNTgsInZpZCI6IjBmMWMyNTExLTg2YTItNGMxNi05NWU0LTAxMzJjZGYyYjM0NSIsImhvbWVwYWdlIjp7fX1nUDJTeEpQK0ZNYjZKN25UeWNCNnhEUVYxMTAzVVBzRVV5aUkyNFQ4RmRJPQ.MQ',
    '_etc': 'mhT3x3iOvdtDf7VF',
    'x-available-ae': 'ecom-daily',
    '_gcl_au': '1.1.1199213278.1675343140',
    '_ga': 'GA1.2.5464364.1675343141',
    '_scid': 'b369cce3-6253-43ff-8cce-f328062cdf80',
    '_fbp': 'fb.1.1675343157753.97791858',
    '_sctr': '1|1675276200000',
    'AKA_A2': 'A',
    'ak_bmsc': '22087C5D22250DC8AD1ECEF37ACB3C25~000000000000000000000000000000~YAAQPQVaaAzIIBOGAQAAJMXxJRKtszl1riVpjiJ2rv34/MKeVBynTwLMQejWi+04j52HL3vhfGyeeE/Bsd1zJdDwlCaLfHxEB11hQMNYZIuql//+8Skvn5NuvGycT7AKeLePp1/CS5AACUX7pfU4F77CCjLKUQXcGzrROqmXWB5Ujpq5ph1RfQIrXub3dXPzMd/wLb2Bp2XRBWcL77Bx3o078OxCBAU7MD32xLnNEx9uusl40360VIt2b6omn9T1Se9digZ8c5z2g/5n3CSB2zJffhniI0faXnivYScUTs5OkILSO4n18IoOonm/fSbnhqK5mnUniJVKeX0r5o8o0aOJi13eYATkFy3Jr1aNIpIyr71MUo3sO+qsR2oSaYdnTUJ+fHgtzZXOnKPDpHwXwAb3cnwbsjz0WvFDOR4Ozph115k=',
    'bm_mi': '8FF90313A1FD4A6C6BF3296185D9C4F1~YAAQPQVaaLjFIBOGAQAA0EDxJRJKWt4VuK3OOkLor0Xjh43NmwKDAvpK2iSmEyqyvNJiAog+mLvKpvfXF1OXE/ziGieDy1KO/ItlMRcJaTYhfW/cqyBb7Dt0NPt5yQs+dYM3N2Wg/JSUs6JxjAiID3qvE7+vOR5RMFNqJhmsu/f4HhcARhgXqVk4q5I9X+yd84GWDt2z5MDJK5QYojBMvsDTW3Dj7U4hM66iSdH5J1pOvCBDj0PbM37sfqHUQZU4FlkXvP9UgHXVYupcMPmlq/xTSRXed9F/3qIdgdsd7j0BRqMhMDdocWhQu13yxh+ff74=~1',
    'bm_sv': '1D808F86D032C3B10633985F291970B6~YAAQPQVaaDgkIhOGAQAA88QXJhJSMo9Kp+Dd1e07aMlf/PolXVPH5VrAxfYuWnS6NhS2IVO+c/PSrcsV5T86XwrUXI2je2B1Nquz1uwswJ3YtIVYMVRx6sSBaAafiepgbUxuOkzzALvpx4SMo0DmJqPasNyAa7EP3s7VQvvvsHW05QS39BjxpRDD7nVHo8jjPXy1Fagno3yDKpnjY8edqaXz51QuxH1gMRN5/hr5wXd/10Q+zkkcXrXyIOmcENw=~1',
    '_gid': 'GA1.2.577882318.1675673818',
    '_tt_enable_cookie': '1',
    '_ttp': 'TrI6gT1dgDJt4xnP4mLpqJc1toA',
    '__zlcmid': '1EIla7IZQ8zsZt5',
    '__gads': 'ID=f2ad88a6238e2d70:T=1675673882:S=ALNI_MYR7_ZBC6qBCnzBFNpKb1xab7sZ0w',
    '__gpi': 'UID=00000bb69ede8da7:T=1675673882:RT=1675673882:S=ALNI_MYrLHAHdAeVspNnFG3g5Vqgcnyu8A',
    '_gat_UA-84507530-14': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.noon.com/uae-en/hp/?limit=50&page=2&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc',
    'x-locale': 'en-ae',
    'x-content': 'desktop',
    'x-cms': 'v3',
    'x-mp': 'noon',
    'x-platform': 'web',
    'x-lat': '25.1998495',
    'x-lng': '55.2715985',
    'x-aby': '{"back_in_stock.back_in_stock":1,"delivery_estimates_v2.show_new_estimates":1,"golazo.enabled":1,"ipl.enabled":1,"ipl_entrypoint.enabled":1,"navpills_with_icons.navpills_with_icons":1,"recommendations.recommendations_pdp_toggle":1,"show_ar_model.enabled":1,"wishlist_experiment_entrypoint.entry_point_wishlist":2,"wishlist_toggle.wishlist_toggle":true,"wishlist_toggle_v2.enabled":true}',
    'Connection': 'keep-alive',
    # 'Cookie': 'visitor_id=0f1c2511-86a2-4c16-95e4-0132cdf2b345; RT="z=1&dm=noon.com&si=fbtqs13mucf&ss=ldskx8ki&sl=2&tt=2tv&rl=1&obo=1&ld=u511&r=37945691e91569bc1239898c31ce26b7&ul=u519&hd=u55j&nu=d41d8cd98f00b204e9800998ecf8427e&cl=1j2dp"; nguest=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnJhV1FpT2lJeE1qUTNNR1E1WkdVeU9USTBaamt5WW1ZM1pUVTJNV001TUdZMlptSXpPQ0lzSW1saGRDSTZNVFkzTlRNME16RXpPWDAuN0kzOVpRdzR0SjVDTzhtT25HN3lDNUZhYkJkY0I0NW95ak50YTFnczB5dyIsImlhdCI6MTY3NTY3NjE1OH0.NiKin5tRnMmsJxuAZMoRnS2mowyY3LPBznPHsHTGCmA; _nsc=nsv1.public.eyJzdGlkIjoiMmJiNzJlOGItYjk5My00NDlmLTg3OWItMmVjYmE4NGYzZjkxIiwic2lkIjoiMTI0NzBkOWRlMjkyNGY5MmJmN2U1NjFjOTBmNmZiMzgiLCJpYXQiOjE2NzU2NzYxNTgsInZpZCI6IjBmMWMyNTExLTg2YTItNGMxNi05NWU0LTAxMzJjZGYyYjM0NSIsImhvbWVwYWdlIjp7fX1nUDJTeEpQK0ZNYjZKN25UeWNCNnhEUVYxMTAzVVBzRVV5aUkyNFQ4RmRJPQ.MQ; _etc=mhT3x3iOvdtDf7VF; x-available-ae=ecom-daily; _gcl_au=1.1.1199213278.1675343140; _ga=GA1.2.5464364.1675343141; _scid=b369cce3-6253-43ff-8cce-f328062cdf80; _fbp=fb.1.1675343157753.97791858; _sctr=1|1675276200000; AKA_A2=A; ak_bmsc=22087C5D22250DC8AD1ECEF37ACB3C25~000000000000000000000000000000~YAAQPQVaaAzIIBOGAQAAJMXxJRKtszl1riVpjiJ2rv34/MKeVBynTwLMQejWi+04j52HL3vhfGyeeE/Bsd1zJdDwlCaLfHxEB11hQMNYZIuql//+8Skvn5NuvGycT7AKeLePp1/CS5AACUX7pfU4F77CCjLKUQXcGzrROqmXWB5Ujpq5ph1RfQIrXub3dXPzMd/wLb2Bp2XRBWcL77Bx3o078OxCBAU7MD32xLnNEx9uusl40360VIt2b6omn9T1Se9digZ8c5z2g/5n3CSB2zJffhniI0faXnivYScUTs5OkILSO4n18IoOonm/fSbnhqK5mnUniJVKeX0r5o8o0aOJi13eYATkFy3Jr1aNIpIyr71MUo3sO+qsR2oSaYdnTUJ+fHgtzZXOnKPDpHwXwAb3cnwbsjz0WvFDOR4Ozph115k=; bm_mi=8FF90313A1FD4A6C6BF3296185D9C4F1~YAAQPQVaaLjFIBOGAQAA0EDxJRJKWt4VuK3OOkLor0Xjh43NmwKDAvpK2iSmEyqyvNJiAog+mLvKpvfXF1OXE/ziGieDy1KO/ItlMRcJaTYhfW/cqyBb7Dt0NPt5yQs+dYM3N2Wg/JSUs6JxjAiID3qvE7+vOR5RMFNqJhmsu/f4HhcARhgXqVk4q5I9X+yd84GWDt2z5MDJK5QYojBMvsDTW3Dj7U4hM66iSdH5J1pOvCBDj0PbM37sfqHUQZU4FlkXvP9UgHXVYupcMPmlq/xTSRXed9F/3qIdgdsd7j0BRqMhMDdocWhQu13yxh+ff74=~1; bm_sv=1D808F86D032C3B10633985F291970B6~YAAQPQVaaDgkIhOGAQAA88QXJhJSMo9Kp+Dd1e07aMlf/PolXVPH5VrAxfYuWnS6NhS2IVO+c/PSrcsV5T86XwrUXI2je2B1Nquz1uwswJ3YtIVYMVRx6sSBaAafiepgbUxuOkzzALvpx4SMo0DmJqPasNyAa7EP3s7VQvvvsHW05QS39BjxpRDD7nVHo8jjPXy1Fagno3yDKpnjY8edqaXz51QuxH1gMRN5/hr5wXd/10Q+zkkcXrXyIOmcENw=~1; _gid=GA1.2.577882318.1675673818; _tt_enable_cookie=1; _ttp=TrI6gT1dgDJt4xnP4mLpqJc1toA; __zlcmid=1EIla7IZQ8zsZt5; __gads=ID=f2ad88a6238e2d70:T=1675673882:S=ALNI_MYR7_ZBC6qBCnzBFNpKb1xab7sZ0w; __gpi=UID=00000bb69ede8da7:T=1675673882:RT=1675673882:S=ALNI_MYrLHAHdAeVspNnFG3g5Vqgcnyu8A; _gat_UA-84507530-14=1',
    'If-None-Match': 'W/"1299a-hKOZ0YdMdt7Co5HEtUlknXlhKI4"',
    'TE': 'Trailers',
}

params = {
    'limit': '50',
    'page': '{}',
    'sort[by]': 'popularity',
    'sort[dir]': 'desc',
}

response = requests.get('https://www.noon.com/_svc/catalog/api/v3/u/hp/', params=params, headers=headers)

def list_page(url):
    js=response.json()
    product=js['hits']

    for i in product:
        url="https://www.noon.com/"+i.get['url']+'/'+i.get['plp_product_group_code']+'/p/?o='+i.get['offer_code']
        title=i.get('name')
        # print(url)
        sku=i.get('sku')
        price=i.get('price')
        sale_price=i.get('sale_price')
        specification=i.get('plp_specifications')
        data={
            'ulr':url,
            'title':title,
            'sku':sku,
            'price':price,
            'sale':sale_price,
            'specification':specification

        }  

        l.append(data)
        print(l)  
        
for i in range(1,10):
    url="https://www.noon.com/uae-en/hp/?limit=50&page=2&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc"
    r=s.get(f"https://www.noon.com/uae-en/hp/?limit=50&page={i}&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc")
    js=r.json()
    product=js['hits']
    m=[]
    for i in product:
        url="https://www.noon.com/"+i.get['url']+'/'+i.get['plp_product_group_code']+'/p/?o='+i.get['offer_code']
        title=i.get('name')
        list_page(url)
    
    

# df=pd.DataFrame(l)
# df.to_excel("noon.xlsx",index=False)




# url=https://www.noon.com/uae-en/hp/?limit=50&page=2&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc
# url=https://www.noon.com/uae-en/hp/?limit=50&page=3&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc

# api=https://www.noon.com/_svc/catalog/api/v3/u/hp/?limit=50&page=2&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc

# js['hits'][0]['url'] + '/' + js['hits'][0]['plp_product_group_code'] + '/p/

# https://www.noon.com/2-piece-original-305-black-and-tri-colour-ink-cartridge-set-black-multicolor/N43983194A/p/?o=d9e041b9dfbadb8b
# https://www.noon.com/2-piece-original-305-black-and-tri-colour-ink-cartridge-set-black-multicolorN43983194A/p/d9e041b9dfbadb8b

# for i in js['hits']:
#     link = i['url']+'/'+i['plp_product_group_code']+'/p/?o='+i['offer_code']
#     print(link)