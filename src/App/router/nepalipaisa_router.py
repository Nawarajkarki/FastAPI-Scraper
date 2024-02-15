from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime, date


from src.entrypoint.database import get_db
from src.App.services.nepaliPaisa_services import ScrapeCompany, DailyPriceService
from src.App.schemas import nepaliPaisa_schemas

stocks = APIRouter(prefix='/api/stocks')


@stocks.get('/price/')
def get_today_price(symbol:str, date:date = date.today(), db:Session=Depends(get_db)):
    daily_price = DailyPriceService(db)
    
    data = daily_price.todays_price(symbol=symbol.upper(), date=date)
    return data

@stocks.get('/companies', response_model=list[nepaliPaisa_schemas.Company])
def get_all_companies(db:Session=Depends(get_db)):
    comp_service = ScrapeCompany(db)
    companies = comp_service.get_all_companies()
    return companies



@stocks.get('/companies/{symbol}', response_model=nepaliPaisa_schemas.Company)
def get_company_by_symbol(symbol, db:Session=Depends(get_db)):
    comp_service = ScrapeCompany(db)
    company = comp_service.get_company_by_symbol(symbol)
    return company
    
    pass





scraper = APIRouter(prefix='/api/scraper/nepalipaisa', tags=['Scraper'])


@scraper.get('/company')
def scrape_company(db:Session=Depends(get_db)):
    scraper = ScrapeCompany(db)
    scraper.scrape_company_and_add_to_db()
    return "scraped"
    
    
@scraper.get('/dailyPrice')
def scrape_daily_stock_prices(db:Session=Depends(get_db)):
    scraper = DailyPriceService(db)
    scraper.daily_share_price()
    return "scraped"


@scraper.post('/dp/')
def manual_add_today_price(data : nepaliPaisa_schemas.DailyStockPriceCreate, db:Session=Depends(get_db)):
    service = DailyPriceService(db)
    
    data = service.add_new_data(data)
    return data