from bs4 import BeautifulSoup as bs
from requests import Session
s = Session()
import pandas as pd

import requests

cookies = {
    '_abck': 'F4E719FED9784BF5B12355D9A702A5E1~0~YAAQx2PUF14XAdKFAQAAwVEeAglES9huDyfuLSrbSxggi2xgGGK/PfC8gOHOdxdXcW8bbo2Qw69FzFy0Pa2tpHaiwPDVvqossPQPkZggm5q/d+rCeImC/LZgDAcfcvy2Rn3v4OXsZ0WpMZgm5zp//s3C1mxw1ESJ85dICyUG1NRMpYh9RGx/Ma9tsnOP8u3m6VssRIBgKpwPzGYpLGpbPfk7e9fCsgnWWgjhBT5rOrd+zLLReD5/as+BHpd1OON8hI5VTREM1fgRrE7C5B1Bn6la2otrlEfbxauJF6LAt8SHC42Bmf5DCVmyIsVk3Igi0qqvmJsHix3pZkIuuGqhc4EJAsK1vxhAqH0wwHPJpBZYfRGESTlif14TY711TUP4Rasvt/+XYBSu1ZlxjJcGaonezDcgLLf7ug==~-1~^|^|1-ChJIeyTDPZ-1-10-1000-2^|^|~1675076325',
    'ak_bmsc': 'CE7CAC9E6874A92B307C28BB60EC5D12~000000000000000000000000000000~YAAQx2PUF/sWAdKFAQAAhE8eAhKsXw6ZQ1TnJFLRIahfdVLUP9DnuIweobUJtoEv06FCThIJx6z0dLfEiGgYaCMc5PcQkf6Ye1+9b/6A/AmsC7CFJNXnq+h5Wr089+VgT7/9OZBjyIy/k0oY4+RAvYj8e+hJV5cZU59ghgDP+npRPYbKD00VAKXOlS42JGrU6EJax4/LwEAGncO6ZUiOApj4Nj6dYJRxZgRoJJJDLbocYz6I+r3qhXsHcmGQ3ONenORj/d7hyYRAvuJ/zfwRe2SnuM/uoVzJPnh57zlcsAGFOOYYXCdPK6LY0a7rudMGVmw2W60n/jTX/LDMynIyH4/sjI7VoJUMp1lHhgOOKUgsWZQhQwhxuEdyVco5UZ2n24fV5kAvNZ+mws/InLeDq7p9DWpvnQEmvj/cgskzt95Ew1mzxYaX+FOdUoTElCiJmylqKFW1UId51noWMLJfu1uT3CEBKCcuO0TuQOR3fkdqPyjzSCG58ZIgwQQD',
    'bm_sz': '6EBF0B895DC0CDEC81484A876B26870B~YAAQx2PUF+MVAdKFAQAAP0oeAhJ4sosxJm+Dr0Rc+cz30OVOEuIVxNXE2hqnbbiDP8PTO77wQJexli6nm3Wae8AQAjkzqbmpYlCoMH75PoQx5QCxCTE1WXynoZ0ijveUdo1sKX4OPkFwuVmFFBGxYiyahwnRc7Z6uzxXn14eBRd7YDbrxaXEr4rAComjoDbEMEs311MgYCw0zSaxdSPwU8PZVk0LZowbDHePQLhru8JQh5oMHHzgumSBP5HIx55Hp7U/u+BaP+VWjY+BtpKEYuY7Bb4ndOut34MBP3itBMg7xHg=~4473653~3228228',
    '_d_id': '2991fb18-0900-4c56-bbde-a9ca5a582b14',
    '_ma_session': '^%^7B^%^22id^%^22^%^3A^%^2207fb39e4-4909-4846-910b-b6d047ad9b70-2991fb18-0900-4c56-bbde-a9ca5a582b14^%^22^%^2C^%^22referrer_url^%^22^%^3A^%^22^%^22^%^2C^%^22utm_medium^%^22^%^3A^%^22^%^22^%^2C^%^22utm_source^%^22^%^3A^%^22^%^22^%^2C^%^22utm_channel^%^22^%^3A^%^22^%^22^%^7D',
    'mynt-eupv': '1',
    '_mxab_': 'config.bucket^%^3Dregular^%^3Bcheckout.share^%^3Ddisabled^%^3Bpdp.expiry.date^%^3Denabled^%^3Bcart.discount.expirytimer^%^3Denabled^%^3Bshl.desktop^%^3Denabled-3',
    '_pv': 'default',
    'dp': 'd',
    'at': 'ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pWkRReU5UTTNZMll0WVRBNE5DMHhNV1ZrTFdFMU5UUXRaakkwTlRBME4yVmhORGhpSWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUyT1RBMk1qUTNPRGNzSW1semN5STZJa2xFUlVFaWZRLnBVZzZUZm10SV9LV2FlMkFmZi10TVhuV0ZWMUNKTVJwV2ZVZXN2azdoQkk=',
    'microsessid': '301',
    'lt_timeout': '1',
    'lt_session': '1',
    'utrid': 'VllxFFR6a34NYQxyUwtAMCM2ODA0MDczMjIkMg^%^3D^%^3D.fb39406c8c24d405768890a855a23a39',
    '_xsrf': 'KAIzKOH3Su2vzxlB2Xvz7MVyuFvX4jXg',
    'user_session': 'anOgIKZz6pYNz8iHHiXttw.r-_1B0PkCEpuHRal21GfX1HqCf_GnL1tWh_-v3dG0ndVAxcSAhpIMprOH8Bn3IIdFyo3xoh6a0XnUc8jPFJDoPpCq_2toZ0yemLDn9GgSj6pj8IzUDt3qQcFv5_6PrLrzxvDrjMYOocFQMWhKozMug.1675072785828.86400000.97bF9gteTgpTyULGuCaAbwQk5kjeJwjAIMp_i1kW-5g',
    'bm_sv': '5762B8822D9301A95BAECF630E904F5B~YAAQx2PUF62VAdKFAQAAEqUgAhI9M1ieain3cMkW8OyM6kNs+55vsQXlQ4Q2+y+sKz/CzDAU+kXuKwcf/8/vkYRbJZCWrp46iGVLiB0agx5YnfohoyCiZKclMycqsFqupz5shU6nsO+rgNOD88xY34abQglciyYl1RaLcNBiDsDe5zGYNAk5tpSs9/GX5xot0r5p4RKfOoedYWxeipXfWI8eMtGplPVApHhfYP7x29v6ml0pRPdexs+HnjNAcTtxdg==~1',
    '_gcl_au': '1.1.320596326.1675072785',
    'ak_RT': 'z=1&dm=myntra.com&si=d037e358-81cd-4381-9021-f78557247b8f&ss=ldin33oi&sl=2&tt=36x&obo=1&rl=1',
    'AMP_TOKEN': '^%^24NOT_FOUND',
    'mynt-ulc-api': 'pincode^%^3A110003',
    'mynt-loc-src': 'expiry^%^3A1675074226389^%^7Csource^%^3AIP',
    '_ga': 'GA1.2.740273494.1675072787',
    '_gid': 'GA1.2.1371077851.1675072787',
    'tvc_VID': '1',
    '_fbp': 'fb.1.1675072787445.1982086057',
    'cto_bundle': '-tVliV96OWxmMnY0S29YWWdDejNjRTlqRzVGNzhVUHZ0UlFvTDU4M3FGc2VxdzQ1dDY1ckRTR1I0YkJad2llZmpvNGExeGtlRzhjQmxob2Y3WDl0QzBUeXAlMkY5bkFFQW5KTHM0ZCUyRjNsa21EV3RRaVZERmNiZmdSelcyR0lra053T3FHMkklMkZPTmFROTFaVzlTcnp0RCUyRnZSSHF3ZyUzRCUzRA',
    'AKA_A2': 'A',
    'trackmyvisits': '66b216b96ebe3',
    '_gat': '1',
}


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.myntra.com/men-tshirts?p=3',
    'X-myntraweb': 'Yes',
    'X-Requested-With': 'browser',
    'x-location-context': 'pincode=110003;source=IP',
    'x-meta-app': 'channel=web',
    'Content-Type': 'application/json',
    'app': 'web',
    'x-myntra-app': 'deviceID=2991fb18-0900-4c56-bbde-a9ca5a582b14;customerID=;reqChannel=web;',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
}

params = {
    'p': '1',
    'rows': '50',
    'o': '0',
    'plaEnabled': 'false',
    'xdEnabled': 'false',
    'pincode': '',
}

response = requests.get('https://www.myntra.com/gateway/v2/search/men-tshirts', params=params, cookies=cookies, headers=headers)
url="https://www.myntra.com/men-tshirtss"
js=response.json()
l=[]
product=js['products']
for i in product:
    r = s.get(url,verify = False)
    links="https://www.myntra.com/men-"+i.get('landingPageUrl')
    # print(links)
    title=i.get('productName')
    rating=i.get('rating')
    searchImage=i.get('searchImage')
    discount=i.get('discount')
    sizes=i.get('sizes')
    productId=i.get('productId')
    primaryColour=i.get('primaryColour')
    Discount=i.get('discountDisplayLabel')
    bestPrice=i.get('bestPrice')
    couponCode=i.get('couponCodes')
    # images=i.get('images')[0].get('scr')
    # for i in js['products']:
    #     print(i['images'][0]['src'])
    
    data={
        'links':links,
        'title':title,
        'rating':rating,
        'searchImage':searchImage,
        'discount':discount,
        'sizes':sizes,
        'productId':productId,
        'primaryColour':primaryColour,
        'Discount':Discount,
        'bestPrice':bestPrice,
        'couponCode':couponCode
        # 'images':images
            
    }
    
    l.append(data)
    print(l)
    
    
df=pd.DataFrame(l)
df.to_excel("myntraaa.xlsx",index=False)
    




# https://www.myntra.com/gateway/v2/search/men-tshirts?p=2&rows=50&o=49&plaEnabled=false&xdEnabled=false&pincode=