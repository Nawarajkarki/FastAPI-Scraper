from datetime import datetime


from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from .daraz_scraper_utils.scraper import scrape_page_items
from .daraz_scraper_utils.filters import search_item
from src.App.schemas.daraz_schemas import DarazProductCreate


def launch_headless_browser():
    options = Options()
    options.add_argument('-headless')  # Enable headless mode
    driver = webdriver.Firefox( options=options)
    driver.maximize_window()
    return driver





def main(query):
    driver = launch_headless_browser()
    # driver = webdriver.Firefox()
    # driver.maximize_window()
    url = "https://www.daraz.com.np"
    driver.get(url)
    
    search_item(driver, query)
    
    for item in scrape_page_items(driver):
        # print(item)
        
        data = DarazProductCreate(
            productName = item['title'],
            price = item['price'],
            free_delivery= item['free delivery'],
            ratings = item['ratings'],
            num_of_ratings = item['num of ratigns'],
            total_sold= item['total_sold'],
            url = item['url'],
        )
        yield data




# if __name__ == "__main__":
#     for item in main('mouse'):
#         print(item)