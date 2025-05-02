#Tanner Rosenthal
#5/2/25
#Accessing the Phonebook db


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

print("What do you want to do?")
print("1 - Add a contact")
print("2 - Look up a number")
print("3 - Change a number")
print("4 - Delete a contact")

choice = input("Type 1, 2, 3, or 4: ")

if choice == '1':
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    try:
        cursor.execute("INSERT INTO Entries (name, phone) VALUES (?, ?)", (name, phone))
        conn.commit()
        print("Contact added.")
    except sqlite3.IntegrityError:
        print("That name already exists.")

elif choice == '2':
    name = input("Enter name to look up: ")
    cursor.execute("SELECT phone FROM Entries WHERE name = ?", (name,))
    result = cursor.fetchone()
    if result:
        print("Phone number:", result[0])
    else:
        print("No contact found.")

elif choice == '3':
    name = input("Enter name to update: ")
    new_phone = input("Enter new phone number: ")
    cursor.execute("UPDATE Entries SET phone = ? WHERE name = ?", (new_phone, name))
    if cursor.rowcount == 0:
        print("Name not found.")
    else:
        conn.commit()
        print("Number updated.")

elif choice == '4':
    name = input("Enter name to delete: ")
    cursor.execute("DELETE FROM Entries WHERE name = ?", (name,))
    if cursor.rowcount == 0:
        print("Name not found.")
    else:
        conn.commit()
        print("Contact deleted.")

else:
    print("Not a valid choice.")

conn.close()
