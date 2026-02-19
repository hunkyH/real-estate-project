import logging
import time
from urllib.parse import urljoin
from datetime import datetime

class Yad2:
    
    def fetch_page_data(self, browser, url, retries=3, delay=2):
        for attempt in range(retries):
            try:
                page = browser.new_page()
                page.goto(url, wait_until="domcontentloaded")
                page_data  = page.evaluate("data")
                print(f"Page data: {page_data}")
                return page_data
            except Exception as e:
                logging.error("Error fetching page data (attempt %d/%d): %s", attempt + 1, retries, e)
                if attempt == retries - 1:
                    raise
                time.sleep(delay)
    
    def yad2_scraper(self, browser, url):
        logging.info("Navigated to Yad2 URL: %s", url)
        data = self.fetch_page_data(browser, url)