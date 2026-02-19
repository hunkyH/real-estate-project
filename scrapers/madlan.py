import logging
import time
from urllib.parse import urljoin
from datetime import datetime

class MadlanScraper:
    
    def fetch_page_data(self, browser, url, retries=3, delay=2):
        for attempt in range(retries):
            try:
                page = browser.new_page()
                page.goto(url, wait_until="domcontentloaded")
                script = page.locator("script:has-text('__SSR_HYDRATED_CONTEXT__')").first
                text = script.inner_text()
                ctx = page.evaluate("() => window.__SSR_HYDRATED_CONTEXT__").json_value().get("poi")
                logging.warning(f"Context data: {ctx}")
                return ctx
            except Exception as e:
                logging.error("Error fetching page data (attempt %d/%d): %s", attempt + 1, retries, e)
                if attempt == retries - 1:
                    raise
                time.sleep(delay)
    
    def madlan_scraper(self, browser, url):
        page = self.fetch_page_data(browser, url)
        logging.info("Navigating to URL: %s", url)