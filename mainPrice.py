# mainPrice.py
from scrapePrice import get_price
from storePrice import store_price
from getPrice import get_stored_price
from sendMail import send_email

url = "https://www.agoda.com/vi-vn/flights/results?cid=1922896&tag=7adbeb35-4108-414c-9559-32893b4cdfe5&gclid=Cj0KCQiAqL28BhCrARIsACYJvkdMTm0k-55NDmbqFAgGnYpZ0N0Mx_57G_F24Z6T2EhrmMPj2za7XhYaAvgtEALw_wcB&departureFrom=HAN&departureFromType=1&arrivalTo=SGN&arrivalToType=1&departDate=2025-03-01&returnDate=2025-03-03&searchType=2&cabinType=Economy&adults=2&sort=8"

# Scrape the current price
current_price = get_price(url)
print(f"Scraped price: {current_price}")
if current_price:
    # Compare with stored price
    stored_price = get_stored_price()
    if stored_price:
        if current_price == stored_price:
            # Store the new price
            store_price(url, current_price)
            # Send an email notification
            subject = "Price Change Alert"
            body = f"Get information for this url {url}\n\nThe price has changed!\nNew price: {current_price}\nPrevious price: {stored_price}"
            send_email(
                sender_email="changeme", 
                receiver_email="changeme", 
                password="changeme", 
                subject=subject, 
                body=body
            )
        else:
            print("No price change detected.")
    else:
        print("No stored price found. Adding the current price.")