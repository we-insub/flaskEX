import sqlite3
conn =sqlite3.connect("/home/mato/Downloads/chadwick.db")
print("Opened database successfully")

cursor = conn.execute("SELECT yearID FROM Salaries LIMIT 10")

for row in cursor:
    print("yearID=",row[0])
    
    
