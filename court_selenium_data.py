


######## Answer 1
# from numpy import prod
import pandas as pd

orders = pd.read_csv("orders.csv")
products = pd.read_csv('products.csv')

mg = products.merge(orders[['product_id','net','order_date']])
  

custom_date_data = mg[pd.to_datetime(mg['order_date']).dt.month == 5] 

product = custom_date_data.groupby('product_name').sum().sort_values('net',ascending=False).head(5)
category = custom_date_data.groupby('category_name').sum().sort_values('net',ascending=False).head(5)
subcategory = custom_date_data.groupby('subcategory_name').sum().sort_values('net',ascending=False).head(5)
brand = custom_date_data.groupby('brand_name').sum().sort_values('net',ascending=False).head(5)


print(product)
print(category)
print(subcategory)
print(brand)


################ Answer 2

import pandas as pd

orders = pd.read_csv("orders.csv")
products = pd.read_csv('products.csv')

mg = products.merge(orders[['product_id','net','order_date']])

penetration = []
mg['order_date'] = pd.to_datetime(mg['order_date'])
for i in ["2018-05-01","2018-05-02","2018-05-03","2018-05-04","2018-05-05"]:
    _mg = mg[(mg['order_date'] == i )]
    penetration.append("{:.0%}".format((_mg[_mg['category_name'] == "Milk"].count() / _mg['category_name'].count()).iloc[0]))



print("\n\n\npenetration ouptput...\n",penetration)