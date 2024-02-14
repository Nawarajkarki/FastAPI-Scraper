from datetime import datetime
from fastapi import HTTPException

from src.App.schemas.schemas import CompanyCreate, DailyStockPriceCreate

import requests
import json



def save_to_json(filename, data):
    with open(f'{filename}.json', 'w') as f:
        json.dump(data, f)



def ipo_scraper() -> list[dict]:
    url = "https://www.nepalipaisa.com/api/GetIpos?stockSymbol=&pageNo=1&itemsPerPage=1000&pagePerDisplay=5&_=1707765871906"

    ipo_response = requests.get(url)
    data = ipo_response.json()
    # for each in range(len(data['result']['data'])):
    save_to_json("ipo_response", data['result']['data'])
        
    ## Returns a list of dict
    return data['result']['data']





def live_market_scraper() -> list[dict]:
    url = "https://www.nepalipaisa.com/api/GetStockLive?stockSymbol=&_=1707840239240"
    live_market = requests.get(url)
    
    if live_market.status_code == 200:
        data = live_market.json()
        
        stocks = data['result']['stocks']
    
    save_to_json("liveMarket", stocks)
    
    
    
    

def today_share_price_scraper():
    url = "https://www.nepalipaisa.com/api/GetTodaySharePrice"
    today_share_price = requests.get(url)
    
    if today_share_price.status_code != 200:
        raise HTTPException(status_code=500, detail="Error with scraper")
    
    
    data = today_share_price.json()
    stocks = data['result']['stocks']   
    # save_to_json("TodaySharePrice", stocks)
    
    for each in stocks:
        as_of_date_str = str(each.get('asOfDate'))
        as_of_date = datetime.strptime(as_of_date_str, "%Y-%m-%dT%H:%M:%S") if as_of_date_str else None

        stock = DailyStockPriceCreate(
            symbol = each.get('stockSymbol'),
            date = as_of_date.date(),
            openPrice = each.get('openingPrice'),
            closePrice = each.get('closingPrice'),
            highPrice = each.get('maxPrice'),
            lowPrice = each.get('minPrice'),
            previousClose = each.get('previousClosing'),
            volume = each.get('volume'),
        )
        
        yield stock


    



def scrape_companies():
    url = "https://www.nepalipaisa.com/api/GetCompanies"
    data = []
    
    companies_resp = requests.post(url, json=data)
    
    if companies_resp.status_code != 200:
        raise HTTPException(status_code=500, detail="Error with scraper")
        
        
    json_response = companies_resp.json()
    companies = json_response['result']
    # save_to_json('Companies', companies)
    
    for each in companies:
        company = CompanyCreate(
            name = each.get('companyName'),
            symbol =  each.get('stockSymbol'),
            sector =  each.get('sectorName')
        )
        
        print(company)
        
        yield company

    
        

      

# ipo_scraper()
# live_market_scraper()
# today_share_price_scraper()
# get_companies()