from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import os

class WebScraper:
    def __init__(self, headless=False):
        """Initialize the web scraper with Chrome options."""
        self.options = Options()
        if headless:
            self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        
        # Initialize the Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), 
                                     options=self.options)
        self.wait = WebDriverWait(self.driver, 10)
        
    def search_google(self, query):
        """Search Google for the given query and return search results."""
        print(f"Searching for: {query}")
        self.driver.get("https://www.google.com")
        
        # Accept cookies if the banner appears
        try:
            accept_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "L2AGLb"))
            )
            accept_button.click()
        except:
            pass  # Cookie banner not found or already accepted
        
        # Find the search box and enter the query
        search_box = self.wait.until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.clear()
        search_box.send_keys(query)
        search_box.submit()
        
        # Wait for results to load
        time.sleep(2)
        
        # Extract search results
        results = []
        search_results = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.g"))
        )
        
        for result in search_results[:5]:  # Get top 5 results
            try:
                title = result.find_element(By.CSS_SELECTOR, "h3").text
                link = result.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                snippet = result.find_element(By.CSS_SELECTOR, "div.VwiC3b").text
                results.append({
                    'title': title,
                    'link': link,
                    'snippet': snippet
                })
            except:
                continue
                
        return results
    
    def save_to_csv(self, data, filename='search_results.csv'):
        """Save the scraped data to a CSV file."""
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"Results saved to {os.path.abspath(filename)}")
    
    def close(self):
        """Close the browser."""
        self.driver.quit()

def main():
    # Initialize the scraper
    scraper = WebScraper(headless=False)  # Set headless=True to run without opening browser
    
    try:
        # Example: Search Google and get results
        query = input("Enter your search query: ") or "Selenium Web Scraping"
        results = scraper.search_google(query)
        
        # Display results
        print(f"\nTop {len(results)} search results for '{query}':")
        for idx, result in enumerate(results, 1):
            print(f"\n{idx}. {result['title']}")
            print(f"   {result['link']}")
        
        # Save results to CSV
        scraper.save_to_csv(results, f"{query.replace(' ', '_')}_results.csv")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        # Always close the browser when done
        scraper.close()

if __name__ == "__main__":
    main()
