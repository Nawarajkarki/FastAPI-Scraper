
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




def search_item(driver, query:str):
    wait = WebDriverWait(driver, 15)
    search_bar_xpath = "//input[@id='q']"
    
    search_bar = wait.until(EC.element_to_be_clickable((By.XPATH, search_bar_xpath)))
    actions = ActionChains(driver)
    actions.move_to_element(search_bar).click()
    actions.click()
    search_bar.send_keys(query)
    search_bar.send_keys(Keys.ENTER)
    time.sleep(10)
  