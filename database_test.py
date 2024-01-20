import sqlite3

con = sqlite3.connect("card_database.db")

cur = con.cursor()

cur.execute("CREATE TABLE websites (website_name TEXT, website_ID INTEGER)")
cur.execute("CREATE TABLE products (barcode INTEGER, game_name TEXT, set_name TEXT, product_type TEXT, product_ID INTEGER )")
cur.execute("CREATE TABLE website_urls          (website_ID INTEGER, product_ID INTEGER, URL TEXT, PARSER TEXT)")
cur.execute("CREATE TABLE product_price_history (website_ID INTEGER, product_ID INTEGER, date TEXT, price_base INTEGER, currency TEXT)")


cur.execute("delete from website_urls")

cur.execute("insert into website_urls values (1,53,'https://www.mtggoldfish.com/price/Wilds+of+Eldraine/Wilds+of+Eldraine+Set+Booster+Box-sealed#paper','MTGGOLDFISH')")
cur.execute("insert into website_urls values (1,52,'https://www.mtggoldfish.com/price/Wilds+of+Eldraine/Wilds+of+Eldraine+Draft+Booster+Box-sealed#paper','MTGGOLDFISH')")
cur.execute("insert into website_urls values (1,71,'https://www.mtggoldfish.com/price/Ikoria+Lair+of+Behemoths/Ikoria+Lair+of+Behemoths+Booster+Box-sealed#paper','MTGGOLDFISH')")
cur.execute("insert into website_urls values (1,73,'https://www.mtggoldfish.com/price/Core+Set+2021/Core+Set+2021+Draft+Booster+Box-sealed#paper','MTGGOLDFISH')")

cur.execute("insert into websites values ('MTGGoldfish',1)")


cur.execute("delete from products")

cur.execute("insert into products values (195166102443,'Magic the Gathering','Kamigawa Neon Dynasty','Draft Booster',1)")
cur.execute("insert into products values (195166104980,'Magic the Gathering','Kamigawa Neon Dynasty','Set Booster',2)")
cur.execute("insert into products values (195166105338,'Magic the Gathering','Kamigawa Neon Dynasty','Collector Booster',3)")
cur.execute("insert into products values (195166120195,'Magic the Gathering','Streets of New Capenna','Draft Booster',4)")
cur.execute("insert into products values (195166121048,'Magic the Gathering','Streets of New Capenna - The Brokers','Pre Release ',5)")
cur.execute("insert into products values (195166121925,'Magic the Gathering','Streets of New Capenna','Set Booster',6)")
cur.execute("insert into products values (195166122076,'Magic the Gathering','Streets of New Capenna','Collector Booster',7)")
cur.execute("insert into products values (195166125213,'Magic the Gathering','Modern Horizons 2','Set Booster',8)")
cur.execute("insert into products values (195166128238,'Magic the Gathering','Dominaria United','Collector Booster',9)")
cur.execute("insert into products values (195166128542,'Magic the Gathering','Dominaria United','Draft Booster',10)")
cur.execute("insert into products values (195166129075,'Magic the Gathering','Dominaria United','Set Booster',11)")
cur.execute("insert into products values (195166138817,'Magic the Gathering','Gruul Stompy','Challenger Deck',12)")
cur.execute("insert into products values (195166150581,'Magic the Gathering','The Brothers War','Draft Booster',13)")
cur.execute("insert into products values (195166150604,'Magic the Gathering','The Brothers War','Prerelease',14)")
cur.execute("insert into products values (195166150659,'Magic the Gathering','The Brothers War','Set Booster',15)")
cur.execute("insert into products values (195166151243,'Magic the Gathering','The Brothers War','Collector Booster',16)")
cur.execute("insert into products values (195166152493,'Magic the Gathering','Unfinity','Draft Booster',17)")
cur.execute("insert into products values (195166158327,'Magic the Gathering','Innistrad Double Feature','Draft Booster',18)")
cur.execute("insert into products values (195166168661,'Magic the Gathering','Double Masters 2022','Draft Booster',19)")
cur.execute("insert into products values (195166168951,'Magic the Gathering','Double Masters 2022','Collector Booster',20)")
cur.execute("insert into products values (195166170749,'Magic the Gathering','Unfinity','Collector Booster',21)")
cur.execute("insert into products values (195166173467,'Magic the Gathering','Warhammer 40,000 - Necron Dynasties','Commander',22)")
cur.execute("insert into products values (195166173467,'Magic the Gathering','Warhammer 40,000 - The Ruinous Powers','Commander',23)")
cur.execute("insert into products values (195166173467,'Magic the Gathering','Warhammer 40,000 - Forces of the Imperium','Commander',24)")
cur.execute("insert into products values (195166173467,'Magic the Gathering','Warhammer 40,000 - Tyranid Swarm','Commander',25)")
cur.execute("insert into products values (195166176987,'Magic the Gathering','Jumpstart 2022','Booster',26)")
cur.execute("insert into products values (195166181127,'Magic the Gathering','D&D Battle for Baldurs Gate','Draft Booster',27)")
cur.execute("insert into products values (195166181363,'Magic the Gathering','D&D Battle for Baldurs Gate','Set Booster',28)")
cur.execute("insert into products values (195166181714,'Magic the Gathering','D&D Battle for Baldurs Gate','Collector Booster',29)")
cur.execute("insert into products values (195166182094,'Magic the Gathering','D&D Battle for Baldurs Gate','Pre Release',30)")
cur.execute("insert into products values (195166184845,'Magic the Gathering','Phyrexia All Will Be One','Draft Booster',31)")
cur.execute("insert into products values (195166185019,'Magic the Gathering','Phyrexia All Will Be One','Set Booster',32)")
cur.execute("insert into products values (195166185163,'Magic the Gathering','Phyrexia All Will Be One','Collector Booster',33)")
cur.execute("insert into products values (195166200552,'Magic the Gathering','Dominaria Remastered','Draft Booster',34)")
cur.execute("insert into products values (195166200682,'Magic the Gathering','Dominaria Remastered','Collector Booster',35)")
cur.execute("insert into products values (195166204932,'Magic the Gathering','The Lord of the Rings Tales of Middle Earth','Draft Booster',36)")
cur.execute("insert into products values (195166205007,'Magic the Gathering','The Lord of the Rings Tales of Middle Earth','Set Booster',37)")
cur.execute("insert into products values (195166205038,'Magic the Gathering','The Lord of the Rings Tales of Middle Earth','Collector Booster',38)")
cur.execute("insert into products values (195166207094,'Magic the Gathering','March of the Machine','Draft Booster',39)")
cur.execute("insert into products values (195166207247,'Magic the Gathering','March of the Machine','Set Booster',40)")
cur.execute("insert into products values (195166208350,'Magic the Gathering','March of the Machine','Collector Booster',41)")
cur.execute("insert into products values (195166213903,'Magic the Gathering','March of the Machine : The Aftermath','Collector Booster',42)")
cur.execute("insert into products values (195166216683,'Magic the Gathering','Commander Masters','Collector Booster',43)")
cur.execute("insert into products values (195166216805,'Magic the Gathering','Commander Masters','Set Booster',44)")
cur.execute("insert into products values (195166217208,'Magic the Gathering','Commander Masters','Draft Booster',45)")
cur.execute("insert into products values (195166228846,'Magic the Gathering','Universes Beyond Doctor Who','Collector Booster',46)")
cur.execute("insert into products values (195166229133,'Magic the Gathering','Ravnica Remastered','Draft Booster',47)")
cur.execute("insert into products values (195166229270,'Magic the Gathering','Ravnica Remastered','Collector Booster',48)")
cur.execute("insert into products values (195166229669,'Magic the Gathering','The Lost Caverns of Ixalan','Draft Booster',49)")
cur.execute("insert into products values (195166229874,'Magic the Gathering','The Lost Caverns of Ixalan','Set Booster',50)")
cur.execute("insert into products values (195166229973,'Magic the Gathering','The Lost Caverns of Ixalan','Collector Booster',51)")
cur.execute("insert into products values (195166231631,'Magic the Gathering','Wilds of Eldraine','Draft Booster',52)")
cur.execute("insert into products values (195166231808,'Magic the Gathering','Wilds of Eldraine','Set Booster',53)")
cur.execute("insert into products values (195166231938,'Magic the Gathering','Wilds of Eldraine','Collector Booster',54)")
cur.execute("insert into products values (195166231945,'Magic the Gathering','Wilds of Eldraine','Collector Booster',55)")
cur.execute("insert into products values (630509550609,'Magic the Gathering','Rivals of Ixalan','Booster',56)")
cur.execute("insert into products values (630509571857,'Magic the Gathering','Iconic Masters','Booster',57)")
cur.execute("insert into products values (630509598793,'Magic the Gathering','Dominaria','Booster',58)")
cur.execute("insert into products values (630509632244,'Magic the Gathering','Exquisite Invention','Commander',59)")
cur.execute("insert into products values (630509668564,'Magic the Gathering','Guilds of Ravnica','Booster',60)")
cur.execute("insert into products values (630509673162,'Magic the Gathering','Ravnica Allegiance','Booster',61)")
cur.execute("insert into products values (630509755370,'Magic the Gathering','War of the Spark','Booster',62)")
cur.execute("insert into products values (630509774708,'Magic the Gathering','Core 2020','Booster',63)")
cur.execute("insert into products values (630509777716,'Magic the Gathering','Modern Horizons','Booster',64)")
cur.execute("insert into products values (630509785223,'Magic the Gathering','Throne of Eldraine','Booster',65)")
cur.execute("insert into products values (630509792528,'Magic the Gathering','Theros Beyond Death','Booster',66)")
cur.execute("insert into products values (630509796434,'Magic the Gathering','Commander Legends','Draft Booster',67)")
cur.execute("insert into products values (630509829972,'Magic the Gathering','Throne of Eldraine','Collector Booster',68)")
cur.execute("insert into products values (630509848898,'Magic the Gathering','Theros Beyond Death','Collector Booster',69)")
cur.execute("insert into products values (630509896752,'Magic the Gathering','Mystery Booster (retail edition)','Booster',70)")
cur.execute("insert into products values (630509900497,'Magic the Gathering','Ikoria','Booster',71)")
cur.execute("insert into products values (630509901074,'Magic the Gathering','Ikoria (Japanese)','Draft Booster',72)")
cur.execute("insert into products values (630509902521,'Magic the Gathering','Core 2021','Booster',73)")
cur.execute("insert into products values (630509905461,'Magic the Gathering','Ikoria','Collector Booster',74)")
cur.execute("insert into products values (630509905904,'Magic the Gathering','Zendikar Rising','Draft Booster',75)")
cur.execute("insert into products values (630509907106,'Magic the Gathering','Ikoria (Japanese)','Collector Booster',76)")
cur.execute("insert into products values (630509907625,'Magic the Gathering','Kaldheim','Draft Booster',77)")
cur.execute("insert into products values (630509914753,'Magic the Gathering','Core 2021','Collector Booster',78)")
cur.execute("insert into products values (630509916375,'Magic the Gathering','Zendikar Rising','Pre Release ',79)")
cur.execute("insert into products values (630509917716,'Magic the Gathering','Jumpstart','Booster',80)")
cur.execute("insert into products values (630509917877,'Magic the Gathering','Zendikar Rising','Collector Booster',81)")
cur.execute("insert into products values (630509921768,'Magic the Gathering','Kaldheim','Collector Booster',82)")
cur.execute("insert into products values (630509924745,'Magic the Gathering','Commander Legends','Collector Booster',83)")
cur.execute("insert into products values (630509924936,'Magic the Gathering','Modern Horizons 2','Draft Booster',84)")
cur.execute("insert into products values (630509925568,'Magic the Gathering','Modern Horizons 2','Collector Booster',85)")
cur.execute("insert into products values (630509951529,'Magic the Gathering','Zendikar Rising','Set Booster',86)")
cur.execute("insert into products values (630509957651,'Magic the Gathering','Strixhaven','Draft Booster',87)")
cur.execute("insert into products values (630509958863,'Magic the Gathering','Strixhaven','Collector Booster',88)")
cur.execute("insert into products values (630509971138,'Magic the Gathering','Kaldheim','Set Booster',89)")
cur.execute("insert into products values (630509975679,'Magic the Gathering','Strixhaven','Set Booster',90)")
cur.execute("insert into products values (630509981151,'Magic the Gathering','D&D Adventures in the Forgotten Realms','Draft Booster',91)")
cur.execute("insert into products values (630509982721,'Magic the Gathering','D&D Adventures in the Forgotten Realms','Collector Booster',92)")
cur.execute("insert into products values (630509982875,'Magic the Gathering','D&D Adventures in the Forgotten Realms','Set Booster',93)")
cur.execute("insert into products values (630509984879,'Magic the Gathering','Timespiral Remastered','Draft Booster',94)")
cur.execute("insert into products values (630509986446,'Magic the Gathering','Innistrad Midnight Hunt','Draft Booster',95)")
cur.execute("insert into products values (630509987184,'Magic the Gathering','Innistrad Midnight Hunt','Set Booster',96)")
cur.execute("insert into products values (630509987290,'Magic the Gathering','Innistrad Midnight Hunt','Collector Booster',97)")
cur.execute("insert into products values (630509993468,'Magic the Gathering','Innistrad Crimson Vow','Draft Booster',98)")
cur.execute("insert into products values (630509994489,'Magic the Gathering','Innistrad Crimson Vow','Set Booster',99)")
cur.execute("insert into products values (630509994618,'Magic the Gathering','Innistrad Crimson Vow','Collector Booster',100)")
cur.execute("insert into products values (653569507727,'Magic the Gathering','From the Vault : Relics','From the Vault',101)")
cur.execute("insert into products values (653569933472,'Magic the Gathering','Khans of Tarkir','Booster',102)")
cur.execute("insert into products values (9421905459303,'Flesh and Blood','Welcome to Rathe - Unlimited','Booster',103)")
cur.execute("insert into products values (9421905459327,'Flesh and Blood','Arcane Rising - Unlimited','Booster',104)")


res = cur.execute("SELECT * FROM websites")
 
print (res.fetchall())

res = cur.execute("SELECT * FROM products")
 
print (res.fetchall())



res = cur.execute("SELECT * FROM website_urls")
 
print (res.fetchall())


con.commit()
con.close()