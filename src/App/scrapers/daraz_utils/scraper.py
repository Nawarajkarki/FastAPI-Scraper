import sys
import time
import random
from datetime import datetime


from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException




def scrape_title_price_url(dirver, item):
    title_xpath = ".//div[@id='id-title']"
    title_element = item.find_element(By.XPATH, title_xpath)
    title = title_element.text
    
    
    price_xpaht = ".//div[@class='current-price--Jklkc']//span[@class='currency--GVKjl']"
    price_element = item.find_element(By.XPATH, price_xpaht)
    price = price_element.text
    
    
    items_url_xpath = ".//a[@id='id-a-link']"
    url_element = item.find_element(By.XPATH, items_url_xpath)
    url = url_element.get_attribute('href')

    
    return title, price, url
    pass


def is_free_delivery_available(driver, item):
    free_delivery_xpath = ".//div[@id='id-voucher']/div[@class='free-delivery--OD68c']"
    try:
        free_delivery_tag = item.find_element(By.XPATH, free_delivery_xpath)
        return True
    except (NoSuchElementException, TimeoutException) as e:
        return False
        
    pass


def ratings_and_all(driver, item):
    # Num of ratings scraper try except block
    try:
        ratings_xpath = ".//div[@id='id-rating']//span[@class='ratig-num--KNake rating--pwPrV']"
        rating_element = item.find_element(By.XPATH, ratings_xpath)
        ratings_data = rating_element.text
        ratings = float(ratings_data.split('/')[0])   # Cleaning the ratings data
    except (NoSuchElementException, TimeoutException) as e:
        ratings = None
    
    
    
    # Num of Ratings scraper try except block
    try:
        no_of_ratings_xpath = ".//div[@id='id-rating']//span[@class='rating__review--ygkUy rating--pwPrV']"
        num_of_ratings_element = item.find_element(By.XPATH, no_of_ratings_xpath)
        num_of_ratings_data = num_of_ratings_element.text
        num_of_ratings = int(num_of_ratings_data.strip('()'))   # Cleaning the num of ratings data
    except (NoSuchElementException, TimeoutException) as e:
        num_of_ratings = None

    
    
    
    # Num of items sold scraper try except block
    try:
        no_of_items_sold_xpath = ".//div[@id='id-rating']//div[3]"
        sold_num_element = item.find_element(By.XPATH, no_of_items_sold_xpath)
        items_sold = sold_num_element.text
        # Cleaning the items_sold data
        if 'K' in items_sold:
            items_sold = float(items_sold.replace('K Sold', '')) * 1000
        else:
            items_sold = int(items_sold.replace(' Sold', ''))
    except (NoSuchElementException, TimeoutException) as e:
        items_sold = None
    
    
    return ratings, num_of_ratings, items_sold


def page_navigator(driver):
    pass




def scrape_page_items(driver):
    wait = WebDriverWait(driver, 10)
    
    
    item_xpath = "//div[@class='gridItem--Yd0sa']"
    items = wait.until(EC.presence_of_all_elements_located((By.XPATH, item_xpath)))
    
    
    for item in items:
        driver.execute_script("arguments[0].scrollIntoView();", item)
        
        title, price, url = scrape_title_price_url(driver, item)
        free_delivery = is_free_delivery_available(driver, item)
        ratings, num_of_rating, total_sold = ratings_and_all(driver, item)
        
        # data = [title, price, url, free_delivery, ratings, num_of_rating, total_sold]
        
        data = {
            'title' : title,
            'price' : price,
            'url' : url,
            'free delivery' : free_delivery,
            'ratings' : ratings,
            'num of ratigns' : num_of_rating,
            'total_sold' : total_sold
        }
        
        yield data
    

    
    