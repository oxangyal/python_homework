import sqlite3

try:
    conn = sqlite3.connect('../db/magazines.db')
    print("Successfully connected to magazines.db")
    conn.close()
    print("Database connection closed")
except sqlite3.Error as e:
    print(f"An error occurred: {e}")