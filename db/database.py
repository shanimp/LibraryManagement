import sqlite3

conn = sqlite3.connect("library.db")

print("Database created successfully")

conn.close()