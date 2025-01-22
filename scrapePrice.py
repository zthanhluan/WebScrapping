# scrapePrice.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import re

def get_price(url):
    # Path to your WebDriver executable (e.g., chromedriver)
    service = Service("D:\\NEW_PROJECT\\WebScrapping\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    try:
        # Open the webpage
        driver.get(url)

        # Wait for the JavaScript to render (adjust the time as needed)
        time.sleep(5)

        # Get the fully rendered page source
        html = driver.page_source

        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        all_span = soup.find_all("span")
        
        price_pattern = r"(\d{1,3}(?:\.\d{3})+)"
        # Extract and filter prices from span tags
        matches = []
        for span in all_span:
            if span.string:  # Check if the span contains text
                match = re.search(price_pattern, span.string)
                if match:
                    matches.append(match.group(1))

        # Print all extracted prices
        print("Extracted prices:", matches)

        # Access the first price element
        # Check if any prices were found
        if matches:
            # Extract the first price element (as string)
            price_element = matches[0]

            # Clean and convert the price
            try:
                # Remove formatting and convert to a float
                cleaned_price = float(price_element.replace(".", "").replace(",", "."))
                return cleaned_price
            except ValueError as e:
                print("Error converting price:", e)
                return None
        else:
            print("Price element not found.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        # Ensure the browser is closed
        driver.quit()
