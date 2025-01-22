# getPrice.py
import sqlite3

def create_db():
    # Connect to the SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect("prices.db")
    cursor = conn.cursor()

    # Create a table to store the prices
    cursor.execute('''CREATE TABLE IF NOT EXISTS prices (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        url TEXT NOT NULL,
                        price REAL NOT NULL
                    )''')
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()
    
def get_stored_price():
    
    create_db()
    
    conn = sqlite3.connect("prices.db")
    c = conn.cursor()
    
    c.execute("SELECT price FROM prices ORDER BY id DESC LIMIT 1")
    result = c.fetchone()
    conn.close()
    
    return result[0] if result else None