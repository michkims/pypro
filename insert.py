import sqlite3
conn=sqlite3.connect('emobilis.db')
print("opened db successfully")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES (1,'Erick',30,'eMobilis')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL)VALUES (2,'Chelsea',21,'NHSD')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL)VALUES (3,'Mackenzie',19,'KHG')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL)VALUES (4,'Roland',17,'MHSK')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL)VALUES (5,'Tom',23,'eMobilis')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL)VALUES (6,'Brikston',21,'eMobilis')")

conn.commit()
print("records added successfully")
conn.close()
