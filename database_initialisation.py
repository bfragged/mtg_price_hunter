import sqlite3
import csv

print ("Connecting to SQLite database")
con = sqlite3.connect("card_database.db")

cur = con.cursor()
print ("Clearing Websites, Products and URLS from SQLite database")
cur.execute("delete from website_urls")
cur.execute("delete from products")
cur.execute("delete from websites")

print ("Reloading Websites, Products and URLS from CSVs")
with open('websites.csv', newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in filereader:
        #print (', '.join(row))
        cur.execute("insert into websites values (?,?)",row)

with open('products.csv', newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in filereader:
        #print (', '.join(row))
        cur.execute("insert into products values (?,?,?,?,?,?)",row)
        

with open('website_urls.csv', newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in filereader:
        #print (', '.join(row))
        cur.execute("insert into website_urls values (?,?,?,?)",row)

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

print("Commiting to SQLite database")
con.commit()

con.close()



