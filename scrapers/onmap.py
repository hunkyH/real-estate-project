import logging
import time
from urllib.parse import urljoin
from datetime import datetime

class OnmapScraper:    
    def fetch_page_data(self, browser, url, retries=3, delay=2):
        for attempt in range(retries):
            try:
                page = browser.new_page()
                with page.expect_response(lambda resp:("mixed_search" in resp.url
                    and "option=buy" in resp.url
                    and "section=residence" in resp.url
                    and not "limit=248" in resp.url
                    ), timeout=10000) as response_info:
                    page.goto(url, wait_until="domcontentloaded")
                resp = response_info.value
                if resp.status != 200:
                    raise Exception(f"Unexpected status code: {resp.status}")
                payload = resp.json()
                if not payload.get("data"):
                    raise Exception("Empty data in mixedsearch response")
                return payload.get("data")
            except Exception as e:
                logging.error("Error fetching page (attempt %d/%d): %s", attempt + 1, retries, e)
                if attempt == retries:
                    raise
                time.sleep(delay)
    
    def extract_property_data(self, data, url):
        properties_to_return = []
        try:
            for item in data:
                properties_to_return.append({
                    "source" : "onmap",
                    "id": item.get("id"),
                    "city": item.get("address", {}).get("en", {}).get("city_name"),
                    "price": item.get("price"),
                    "neighborhood": item.get("address", {}).get("en", {}).get("neighborhood"),
                    "street": item.get("address", {}).get("en", {}).get("street_name"),
                    "rooms": item.get("additional_info", {}).get("rooms"),
                    "bathrooms": item.get("additional_info", {}).get("bathrooms"),
                    "size": item.get("additional_info", {}).get("area", {}).get("base"),
                    "url": urljoin(url, item.get("url")),
                    "date_scraped": datetime.now().isoformat()
                })
            return properties_to_return
        except Exception as e:
            logging.error("Error extracting property data: %s", e)
            
    def onmap_scraper(self, browser, url):
        logging.info("Navigating to URL: %s", url)
        page_data = self.fetch_page_data(browser, url)
        all_properties = self.extract_property_data(page_data, url)
        return all_properties