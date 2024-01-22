import sqlite3
import csv

print ("Connecting to SQLite database")
con = sqlite3.connect("card_database.db")

cur = con.cursor()



print ("Saving Websites, Products and URLS to CSVs")
res = cur.execute("SELECT * FROM websites")
with open('websites.csv','w',newline='') as csvfile:
    url_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    url_writer.writerows(res.fetchall())

res = cur.execute("SELECT * FROM products")
with open('products.csv','w',newline='') as csvfile:
    url_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    url_writer.writerows(res.fetchall())
 
res = cur.execute("SELECT * FROM website_urls")
with open('website_urls.csv','w',newline='') as csvfile:
    url_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    url_writer.writerows(res.fetchall())

res = cur.execute("SELECT * FROM product_price_history")
with open('product_price_history.csv','w',newline='') as csvfile:
    url_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    url_writer.writerows(res.fetchall())


print("Commiting to SQLite database")
con.commit()

con.close()



