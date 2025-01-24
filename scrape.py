import selenium.webdriver as webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from bs4 import BeautifulSoup

def scrapWebsite(website):

    options = Options()
    
    #headless Browsing
    options.add_argument("--headless")
    # Specify Firefox binary location if needed
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe" 
    
    # Path to the firefox WebDriver and Profile
    profile = FirefoxProfile(r"C:\\Users\\luan.vt\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\q4cekwng.default-release") 
    options.profile = profile  # Assign the profile object
    firefoxDriver_path = "./geckodriver.exe"
    
    service = Service(firefoxDriver_path) 
    driver = webdriver.Firefox(service=service, options=options)
    
    try:
        driver.get(website)
        print("page loaded ..")
        html = driver.page_source
        return html
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return "Nothing"
    
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content
    
def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]