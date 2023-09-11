import requests
from datetime import datetime
import datatbase_manager
import pandas
import concurrent.futures
import re
from bs4 import BeautifulSoup as BS

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"}


def crawl_listpage(category_url, listpage_collection):
    count = 23
    skip = 0
    page_count = 1
    while True:
        response = requests.get(
            category_url.format(count, skip), headers=headers)
        json_data = response.json()
        if not json_data:
            break
        if type(response.json()) == list:
            products = json_data
        else:
            products = response.json().get('products')
        for product in products:
            url = 'https://www.fjellsport.no' + product.get('url')
            search_query = {"CategoryUrl": category_url.split('?')[0], "Url": url}
            if datatbase_manager.get_records(listpage_collection, search_query):
                continue
            raw = {
                "CategoryUrl": category_url.split('?')[0],
                "Url": url,
                "Sku": product.get('sku'),
                "pageCount": page_count,
                "Name": product.get('displayName'),
                "Brand": product.get('brand'),
                "sellingPrice": product.get('price').get('current').get('inclVat') if product.get('price') else '',
                "originalPrice": product.get('price').get('regular').get('inclVat') if product.get('price') else '',
                "Images": product.get('images')[0].get('url') + '?preset=tiny&dpr=2' if product.get('images') else '',
                "Rating": product.get('rating')
            }
            listpage_collection.update_one({"CategoryUrl": category_url.split('?')[0], "Url": url}, {'$set': raw}, upsert=True)
            # print(f"Completed !!!{page_count}")
        print("pageNo :- ",page_count)
        page_count += 1
        skip = count
        count += 24
    print(f"Category Url:- {category_url.split('?')[0]}")


def crawl_detailpage(url, category_url, listpage_collection):
    response = requests.get(url, headers=headers)
    try:
        description = BS(re.search('"description":"(.*?)","', response.text).group(1), 'html.parser').text.replace('\\n', ' ').strip()
    except:
        description = ""    
    listpage_collection.update_one({"CategoryUrl": category_url, "Url": url}, {'$set': {"Description": description}})
    print(f"DetailPage:- {url}")


def main():
    db_client = datatbase_manager.get_client()
    listpage_collection = db_client['fjellsport']
    start_time = datetime.now()
    categories = ['dameklaer', 'herreklaer']
    for category in categories:
        category_url = 'https://www.fjellsport.no/api/content/__CATEGORYNAME__?count={}&skip={}'.replace('__CATEGORYNAME__', category)
        crawl_listpage(category_url, listpage_collection)
    products = pandas.DataFrame(listpage_collection.find({}))
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for count in range(len(products)):
            url = products.iloc[count].get('Url')
            category_url = products.iloc[count].get('CategoryUrl')
            executor.submit(crawl_detailpage, url, category_url, listpage_collection)

    end_time = datetime.now()
    diff = end_time - start_time
    print("Timing:- ", diff)
