from playwright.sync_api import sync_playwright
from scrapers.onmap import OnmapScraper
from scrapers.madlan import MadlanScraper
from scrapers.yad2 import Yad2
from scrapers.homeless import HomelessScrape
from pipline.normalizer import normalize_listing
from config import BASE_URLS
from datetime import date
from storage.db import get_connection
from storage.schema import init_db
from storage.listing_repo import upsert_listing

def run_pipeline(market : str):
    with sync_playwright() as p:
        normalized_dict = {}
        browser = p.chromium.launch(headless=False)
        homeless = HomelessScrape()
        homeless_properties = homeless.homeless_scraper(browser, url=BASE_URLS["homeless"][market])
        onmap = OnmapScraper()
        onmap_properties = onmap.onmap_scraper(browser, url=BASE_URLS["onmap"][market])
        # yad2 = Yad2()
        # yad2_properties = yad2.yad2_scraper(browser, url=BASE_URLS["yad2"][market])
        # madlan = MadlanScraper()
        # madlan_properties = madlan.madlan_scraper(browser, url=BASE_URLS["madlan"][market])
        browser.close()
        homeless_1 = homeless_properties[0]
        homeless_2 = homeless_properties[1]
    
        scrape_date = date.today().strftime("%Y-%m-%d")
        normalized_dict = []
        for item in onmap_properties:
            normalized_dict.append(normalize_listing(item,scrape_date,market))
        for item in homeless_1:
            normalized_dict.append(normalize_listing(item,scrape_date,market))
        for item in homeless_2:
            normalized_dict.append(normalize_listing(item,scrape_date,market))
        con = get_connection()
        init_db(con)
        for row in normalized_dict:
            upsert_listing(con,row)
        con.commit()
        con.close()