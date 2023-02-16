import sqlite3
conn=sqlite3.connect('emobilis.db')
conn.execute("CREATE TABLE Cars"
             "(ID INT PRIMARY KEY NOT NULL,"
             "NAME TEXT NOT NULL,"
             "YEAR OF PURCHASE INT NOT NULL,"
             "BRAND TEXT NOT NULL)")

print("Table created successfully")
conn.close()

conn.execute("INSERT INTO Cars(ID,NAME,YEAR OF PURCHASE,BRAND)")


