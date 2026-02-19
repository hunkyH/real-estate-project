import logging
import time
from urllib.parse import urljoin
from datetime import datetime

class HomelessScrape:
    
    def fetch_page(self, browser, url, retries=3, delay=2):
        for attempt in range(retries):
            try:
                page = browser.new_page()
                page.goto(url, wait_until="domcontentloaded")
                return page
            except Exception as e:
                logging.error("Error fetching page (attempt %d/%d): %s", attempt + 1, retries, e)
                if attempt == retries:
                    raise
                time.sleep(delay)
    
    def extract_property_data(self, page, url):
        propertys_to_return = []
        try:
            property_main_result = page.locator("table#mainresults").locator("tr[type='ad']").all()
            property_related_results = page.locator("table#relatedresults").locator("tr[type='ad']").all()
            for element in property_main_result:
                try:
                    
                    type = element.locator("td").all()[2].inner_text()
                    city = element.locator("td").all()[3].inner_text()
                    neighborhood = element.locator("td").all()[4].inner_text()
                    street = element.locator("td").all()[5].inner_text()
                    rooms = element.locator("td").all()[6].inner_text()
                    floor = element.locator("td").all()[7].inner_text()
                    price = element.locator("td").all()[8].inner_text()
                    date_updated = element.locator("td").all()[10].inner_text()
                    property_url = urljoin(url, element.locator("a").get_attribute("href"))
                    propertys_to_return.append({
                        "source" : "homeless",
                        "type": type,
                        "city": city,
                        "neighborhood": neighborhood,
                        "street": street,
                        "rooms": rooms,
                        "floor": floor,
                        "price": price,
                        "date_updated": date_updated,
                        "url": property_url,
                        "date_scraped": datetime.now().isoformat()
                    })
                except Exception as e:
                    logging.error("Error extracting data for a property: %s", e)
            for element in property_related_results:
                try:
                    type = element.locator("td").all()[2].inner_text()
                    city = element.locator("td").all()[4].inner_text()
                    neighborhood = element.locator("td").all()[5].inner_text()
                    street = element.locator("td").all()[6].inner_text()
                    rooms = element.locator("td").all()[7].inner_text()
                    price = element.locator("td").all()[8].inner_text()
                    date_updated = element.locator("td").all()[10].inner_text()
                    property_url = urljoin(url, element.locator("a").get_attribute("href"))
                    propertys_to_return.append({
                        "source" : "homeless",
                        "type": type,
                        "city": city,
                        "neighborhood": neighborhood,
                        "street": street,
                        "rooms": rooms,
                        "price": price,
                        "date_updated": date_updated,
                        "url": property_url,
                        "date_scraped": datetime.now().isoformat()
                    })
                except Exception as e:
                    logging.error("Error extracting property data: %s", e)
            return propertys_to_return
        except Exception as e:
            logging.error("Error extracting property data: %s", e)
    
    def click_next(self, page) -> bool:
        next_link = page.get_by_role("link", name="הבא ").filter(has_not=page.locator(".disabled"))
        if next_link.count() == 0:
            return False
        with page.expect_navigation():
            next_link.click()
        return True
    
    def homeless_scraper(self, browser, url):
        logging.info("Navigating to URL: %s", url)
        page = self.fetch_page(browser, url)
        all_propertys = []
        while True:
            all_propertys.append(self.extract_property_data(page, url))
            if not self.click_next(page):
                break
        return all_propertys