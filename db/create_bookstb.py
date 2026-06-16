import sqlite3

conn = sqlite3.connect("library.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    BID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    Author TEXT NOT NULL,
    Category TEXT,
    Publisher TEXT,
    ISBN TEXT UNIQUE,
    Quantity INTEGER DEFAULT 0,
    Price REAL DEFAULT 0,
    AddedDate DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Books table created")