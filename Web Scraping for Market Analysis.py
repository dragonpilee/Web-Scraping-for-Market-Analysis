from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

def scrape_market_data(url):
    # Configure Selenium WebDriver
    options = Options()
    options.add_argument("--headless")  # Run browser in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    
    time.sleep(3)  # Allow time for page to load
    
    products = []
    
    # Locate product elements (Modify these selectors based on target site)
    product_elements = driver.find_elements(By.CSS_SELECTOR, "div.product")
    
    for product in product_elements:
        try:
            name = product.find_element(By.CSS_SELECTOR, "h2.product-title").text
            price = product.find_element(By.CSS_SELECTOR, "span.price").text
            rating = product.find_element(By.CSS_SELECTOR, "span.rating").text
            products.append({"Name": name, "Price": price, "Rating": rating})
        except:
            continue
    
    driver.quit()
    
    return products

if __name__ == "__main__":
    url = "https://example.com/products"  # Replace with target e-commerce URL
    data = scrape_market_data(url)
    df = pd.DataFrame(data)
    df.to_csv("market_data.csv", index=False)
    print("Data scraped and saved to market_data.csv")
