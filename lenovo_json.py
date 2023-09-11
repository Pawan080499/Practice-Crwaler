import requests
from requests import Session
s = Session()
from bs4 import BeautifulSoup as bs
import pandas as pd
# from pymongo import MongoClient

# URl="mongodb://localhost:27017"
# Client=MongoClient(URl)
# mydb=Client['Craling']
# mycol=mydb['Lenovo']


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://www.lenovo.com/in/en/d/deals?IPromoID=LEN512664&sort=sortBy&resultsLayoutType=grid',
    'Cookie': 'akavpau_WaitingRoomController=1674465813~id=4e2c688524ab1d01a589bdd31369ccfe; _abck=98C152E80FB29426EE20CC8C49A33280~0~YAAQjQVaaBGU08WFAQAAgQ7s3QkQ0jmLKCEXiQ6vHPj8ZQQj3gou6lixSAjnDrPlTrmHZdx+bDnNL10/ULLogHtU1a0Vf49cSmyARBIOX8C2SB9lsXXygY6n0lKxwNpnD3veF/1u0KUVNIsIuEpkTJ9vrvyuPjyLP19n/CmWoDNNBAvpsJeNGWSrUYEvFNDkP2wQfp8p/Z/gIEQB7HPXdixDNgN1eO1l/6JnpOSGM07caQlFYUG8t9T22lLNF/yFe1dWQsNDSdc6ReQW/9YAiRt+HQtgmOv8YPy9vwgmvjFsEQubH+LpRRdb+E/3CuLxiqc8gorCoEimT672zQueeMcBoDGxzaycltDrpXDo5mt4IWkMjL/RwQeKZUFRzZ14ud+sOXklz07lYOZJLc/8Y/WsaAEwwRDirQ==~-1~-1~1674468993; bm_sz=144E9D12EEFBA6C3E1686EEAB4DAA670~YAAQvAVaaB+5DNGFAQAAsf3c3RLY7yHAptuzrgawV0x20EGJcZdTX+A7WIX/tE+fuwu/llldv/3blEDoHaXMAFsU0XCsZVg0Ab/VfTXkFps3oK3jpPJcqCbPvHFlfKcK312UhXUYu9Qcl20g2Ogh5Fe3rL4MBBKse9J2qxiuhU9Dd4loB2K8dm808ntF6Z4repojbVgiqeTSSprjnVJq95+zQYCa1YRhGQzjEM80PPw4D0nLna3mBP7Tgc74uzyTsZU6fsMbF9qM/3Tk5Z5pCKrkM3xVhrVrSxG0+i39QUXmRHM=~3618873~3293496; AKA_A2=A; ak_bmsc=BF872CC430DDE3D52223D618743224F8~000000000000000000000000000000~YAAQjQVaaAzy0sWFAQAASQnd3RKiThhQl/JIvG9lJF5OscH0Bh0pZme8z8DJgsiNDFv7BEkCwRXQW+/tGdk+PRGAteXSlQENrXg0eAQwkBoHHtGGtaqc4PrEL821fNKBPKicLr/26BD3j+uA0RF1GG5Q/Fu1lAzpY3tO6KxiQMzqTVoHBelXp7+Mfw0yKfyjoxxCQ49xwS0FsuhuA3N/2Hpua8VmjHYq5mpienR55ZnWf/6J14pgHxg4nqAvDYsCZRIjzT/RA3T/0sz64/qfgxq+e5nyoyt2iRCQgohA67sAD06ChyT7o0VtAiiEJPRpkroSAy17sxu/ueIU1t969lqtejUeZk5Aiey8OXtUx3saOPKSfZs9/52klUGqLl8Tdua+yeOHrpAzIhxuXtXUEiEioJnnSIqWomXbsXI/EkZ2r/Z83kOoCN6wes+lDA15R3QfiiQc4pictb4cE8G5/1/VjR4UbrRxOjZJkN3cSXKE9E/CxaUI73O9zkSG; kndctr_F6171253512D2B8C0A490D45_AdobeOrg_cluster=ind1; kndctr_F6171253512D2B8C0A490D45_AdobeOrg_identity=CiY2NjU5MzA0ODA0MDk4NjgzNjQzMjEzMzU2NDM4ODc1NzM0OTI1MVIRCJ2Q9O7dMBABGAEqBElORDGgAZ2Q9O7dMKgBgreA1t6WlPp58AGdkPTu3TA%3D; AMCV_F6171253512D2B8C0A490D45%40AdobeOrg=MCMID|66593048040986836432133564388757349251; RT="z=1&dm=lenovo.com&si=0a7b322e-d7b5-4344-83a4-e2431951ab9d&ss=ld8kxzia&sl=c&tt=rza&bcn=%2F%2F684d0d49.akstat.io%2F&ld=l94n"; s_tslv=1674465511041; s_inv=0; s_vnc365=1706000528994%26vn%3D1; s_ivc=true; s_dur=1674464528996; s_tot_rfd=2.59; s_eng_rfd=0.00; aamtest1=seg=abc%2Cseg=def%2Cseg=ghi; _gcl_au=1.1.1486637213.1674464529; _ga_EYNZYSHSG4=GS1.1.1674464529.1.1.1674465512.52.0.0; _ga=GA1.2.174289082.1674464530; _mibhv=anon-1674464530081-5564755488_8719; inside-asia=861874488-cc18fba18877b5e6f2f0c38a0fabe17b1b157407b4c974f36f97353c73626bb5-0-0; bluecoreNV=true; _mkto_trk=id:183-WCT-620&token:_mch-lenovo.com-1674464531756-53521; GA1.2.174289082.1674464530; _gid=GA1.2.571632042.1674465515; _fbp=fb.1.1674464532301.1195553791; _ga_LXNLK45HZF=GS1.1.1674464535.1.1.1674465504.0.0.0; _ga_LNFXZCR83J=GS1.1.1674464535.1.1.1674465504.0.0.0; _ga_BWVL3VXBFV=GS1.1.1674464535.1.1.1674465504.0.0.0; bm_sv=F99946276525A3A347FC6A5C40FA060D~YAAQjQVaaPaT08WFAQAACAjs3RLBG4+PI55ET3Oe8ZnOEl1Y96B+GO/WbPFuUmWH2p+AK6INctELYeMLVJTuwF2M4eqdNBGHVnRZK3tstM8sECujaC+hBXMPprYs+BeS306FVHDBZuSMpfmXZiLWHhpQm0W2X2CdlJTyOAunURJmZoNGrn2iXgI/dw9ybzlMOLzJZKpDAi9HRUUnLJzOkMTvOTeH09FBNn56vfiTpaeJco5Xa1dLfR0EFrMfUCnomQ==~1; BVBRANDID=88735f03-e012-4a03-8d9e-df6461ba3dce; BVBRANDSID=2679513d-b24c-4f10-a9fa-ace7bdf99b54; cto_bundle=Gn9YFl8lMkZOa0RFbk1JcHlxY2hvVERkcGs5QTdSeUdjRG9oanFuS082U1BZVEpuem8xUXBYZDRPWjRoTkI0RjZ5RHN1ZzZXcG5KV3IzSkFQVldaYlFLOEE4NXFlR1RPcFUxTlhTM3JseXdJS21KQ01tSlNUWTFnSnkyNUJzckd6SFVmM3lQR1BiMzMxVzg2YUpyQ0FOdndtd2dRUSUzRCUzRA; QuantumMetricSessionID=b5d9b9baffcb530ed60e13f33517e5d8; QuantumMetricUserID=32c9395d2fa3bcade986059b7a3e7398; exitsurveynotdisplayed=Page%20count%20not%20met; LSESSION=CAD056C2-D35D-490C-BD5B-04A15FB30EE5; MSESSIONID=2BC7AAC1AD50F6BEB3DC5CD84E06E956; aam_sc=aamsc=2525370|3245353|3526811|3730438|3245353|7238336|9039690|10170291|10863386|10997626|10170291; JSESSIONID=1B5482B10BF370F8892AA4CF54E0CB11.app11; _uetsid=9e8b09209afc11ed8508016257b8519e; _uetvid=9e8b48709afc11ed86ecb5115316d592; mp_lenovo_in_mixpanel=%7B%22distinct_id%22%3A%20%22185dddd10692c6-0e55d43c2f08378-c5c5429-144000-185dddd106a340%22%2C%22bc_persist_updated%22%3A%201674464530539%7D; bc_invalidateUrlCache_targeting=1674465515337',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

params = {
    'contextString': 'IN|B2C|INWEB|EN_IN',
    'facetFieldsList': '',
    'currency': 'INR',
    'sort': 'sortBy',
    'categories': 'LAPTOPS',
    'page': '1',
    'pageSize': '20',
    'priorityProducts': '82H801L2IN,82KBA02VIH,82K201ULIN,66E8GAC2IN,82R70067IN,82KAA04RIH,4XC1D66055,21E3S03800,82C1002SHA,20VDA047IH,82NL00APIN,66E8GAC2IN,82H801LHIN,82KBA01KIH,GXD1B67867,82KDA00XIH,82K201W6IN,21A1S0RY01,82R9008GIN,65F7GAC1IN,82NC00EWIN,20VDA08RIN,4X30L79883,20VDA08TIN,82SF004WIN,21AAS28B00,82RK0085IN,66CAKAC1IN,82KU017KIN,21E3S02900',
    'partNumbers': '82H801L2IN,82KBA02VIH,82K201ULIN,66E8GAC2IN,82R70067IN,82KAA04RIH,4XC1D66055,21E3S03800,82C1002SHA,20VDA047IH,82NL00APIN,66E8GAC2IN,82H801LHIN,82KBA01KIH,GXD1B67867,82KDA00XIH,82K201W6IN,21A1S0RY01,82R9008GIN,65F7GAC1IN,82NC00EWIN,20VDA08RIN,4X30L79883,20VDA08TIN,82SF004WIN,21AAS28B00,82RK0085IN,66CAKAC1IN,82KU017KIN,21E3S02900,GXC1B34793,82S900HNIN,82LN00JSIN,61DDUAR6WW,82RK00EGIN,4X20M26258,82RB00K8IN,63B4GAR6WW,4XD1C99221,61F1GAR2WW,4Y51C33792,4X41E40077,4X20M26274',
    'cmsFacets': 'facet_Processor,facet_Weight,facet_Price,facet_Color,facet_ScreenSize,facet_Brand,facet_HardDriveSize,facet_HardDrive,facet_Memory,facet_OperatingSystem,facet_Graphics,facet_ScreenResolution,facet_Category,facet_Rating,facet_freeform1,facet_Series,facet_PreloadSW',
}

response = requests.get('https://www.lenovo.com/api/nfe/dlp/search', params=params, headers=headers)

js=response.json()
l=[]
products=js['results']

for i in products:
    pro_url="https://www.lenovo.com/"+i.get('url')
    # print(pro_url)
    name=i.get('name')
    image=i.get('thumbnail')
    stock=i.get('stockCount')
    deliver_time=i.get('leadTimeMessage')
    code=i.get('code')
    ean=i.get('ean')
    m_image="http:"+i.get('galleryPhoto')[0].get('image')
    summary=i.get('summary')
    
    data={
        'pro_url' : pro_url,
        'name' : name,
        'image' : image,
        'stock' : stock,
        'deliver_time' : deliver_time,
        'code' : code,
        'ean' : ean    
    }
    # try:
    #     mycol.insert_one(data)
    #     print(data)
    # except:
    #     pass
    
        
    l.append(data)
    print(l)
    
df=pd.DataFrame(l)
df.to_excel("lenovo.xlsx",index=False)