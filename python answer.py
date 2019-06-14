import numpy as np
import pandas as pd
from datetime import datetime

# Part 1

data = pd.read_excel ("/Users/Kevin/Dropbox/Python/Shoppee_test/Test_Pandas.xlsx")

print (data.head())

columns = data.columns.tolist()

# print(columns)

# Part 2

# a) How many unique shops in dataset
shops = data.shopid.unique()
print("Number of unique shops in dataset: " + str(len(shops)))
print ()

# b) How many unique preferred and cross border shops in the dataset

shoplist = []

for index, row in data.iterrows():
    cb = row['cb_option']
    ispref = row['is_preferred']
    if cb == 1 and ispref == 1:
        shopid = row['shopid']
        if shopid not in shoplist:
            shoplist.append(shopid)

print("Number of unique preferred and cross border shops: " + str(len(shoplist)))
print ()

# c) How many products have zero sold count?

unsold = 0

for index, row in data.iterrows():
    if row["sold_count"] == 0:
        unsold += 1

print("Number of products with zero sold count: " + str(unsold))
print ()

# d) How many products created in the year 2018

products_2018 = 0

for index, row in data.iterrows():
    creation_date = row['item_creation_date'].to_pydatetime()
    if creation_date.year == 2018:
        products_2018 += 1

print("Number of products created in 2018: " + str(products_2018))
print ()


# Part 3

# a) Top 3 preferred shops' shopid have the largest number of unique products

unique_shops = {}

for index, row in data.iterrows():
    if row['is_preferred'] == 1:
        if row['shopid'] in unique_shops:
            unique_shops[row['shopid']] += 1
        else:
            unique_shops[row['shopid']] = 1

top_3_shops = sorted(unique_shops, key = unique_shops.get, reverse = True)[:3]

print("Top 3 shops with the largest number of unique products: " + str(top_3_shops))


# b) Top 3 Categories that have the largest number of unique cross border products

categories_dict = {}

for index, row in data.iterrows():
    if row['cb_option'] == 1:
        if row['category'] in categories_dict:
            categories_dict[row['cateogry']] += 1
        else:
            categories_dict[row['category']] = 1

top_3_shops = sorted(categories_dict, key = categories_dict.get, reverse = True)[:3]

print("Top 3 categories with the largest number of cross-border products: " + str(top_3_shops))

# Part 4: Top 3 shopid with the highest revenue
shop_revenue = {}

for index, row in data.iterrows():
    product_revenue = int(row['sold_count'])* float(row['price'])
    if row['shopid'] in shop_revenue:
        shop_revenue[row['shopid']] += product_revenue
    else:
        shop_revenue[row['shopid']] = product_revenue

top_3_shop_revenue = sorted(shop_revenue, key = shop_revenue.get, reverse = True)[:3]

print("Top 3 shops with the highest revenue: " + str(top_3_shops))
print ()