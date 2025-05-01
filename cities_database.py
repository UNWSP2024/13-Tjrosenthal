#Tanner Rosenthal
#5/1/25
#Cities database Access

import sqlite3

conn = sqlite3.connect('cites.db')

cursor = conn.cursor()

table_name = 'cities'

cursor.execute(f"SELECT * FROM {table_name}")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
