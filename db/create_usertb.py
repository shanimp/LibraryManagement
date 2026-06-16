import sqlite3

conn = sqlite3.connect("library.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    UID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    NIC TEXT,
    UserName TEXT,
    PWD TEXT,
    PWD2 TEXT
)
""")

conn.commit()
conn.close()

print("Books table created")