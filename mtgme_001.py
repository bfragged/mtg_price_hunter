import requests
from bs4 import BeautifulSoup
import sqlite3
import re


con = sqlite3.connect("card_database.db")

cur = con.cursor()


def get_mtggoldfish_price(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"} 
    response = requests.get(url, headers=headers)
    price = None
    if response.status_code == 200: 
        soup = BeautifulSoup(response.text, 'html.parser') # Use BeautifulSoup to extract prices
    
        box_name    = soup.find("div", class_="price-card-image")
        booster_box_name = box_name.text.strip()
        print("price-card-image:'" + booster_box_name + "'" ) 
        
        card_prices = soup.find("div", class_="price-box-price")
        print("price-box-price:" + card_prices.text)
        price = card_prices.text
    else: 
        print("Failed to retrieve the webpage. Check your URL or internet connection.") 
        return None
        
    print (price)
    decimal_price = re.findall('\\d+\\.\\d\\d', price)
    print (decimal_price)
    split_decimal_price = re.findall('\\d+', decimal_price[0])
    price_in_cents = int(split_decimal_price[0]) * 100 + int(split_decimal_price[1])
    print (price_in_cents)
    return (price_in_cents,'USD') 




results = cur.execute("SELECT * FROM website_urls")

for lookup in results.fetchall():
    print (lookup) 
    if lookup[3] == 'MTGGOLDFISH':
        price = get_mtggoldfish_price(lookup[2])
    print (price)
    cur.execute("insert into product_price_history values ({}, {}, '{}', {}, '{}')".format(lookup[0], lookup[1], "2024-01-18",price[0], price[1]))
    con.commit()
    print ("Look up next")
    
    
res = cur.execute("SELECT * FROM product_price_history")
print (res.fetchall())



con.commit()
con.close()