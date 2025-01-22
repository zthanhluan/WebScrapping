# storePrice.py
import sqlite3

def store_price(url, price):
    conn = sqlite3.connect("prices.db")
    c = conn.cursor()
    
    # Create the prices table if it doesn't exist
    c.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY,
            url TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            price TEXT NOT NULL
        )
    """)

    # Insert the price into the table
    c.execute("INSERT INTO prices (url, price) VALUES (?, ?)", (url, price))
    conn.commit()
    conn.close()
    print(f"Stored price: {price} for URL: {url}")

if __name__ == "__main__":
    from scrapePrice import get_price
    price = get_price()
    if price:
        store_price("http://example.com", price)