#Tanner Rosenthal
#5/1/25
#Phonebook database

import sqlite3

conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Entries (
        name TEXT PRIMARY KEY,
        phone TEXT
    )
''')
conn.commit()
conn.close()
