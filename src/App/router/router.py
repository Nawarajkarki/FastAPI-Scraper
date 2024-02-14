from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime, date


from src.entrypoint.database import get_db
from src.App.services.scrape import ScrapeCompany, DailyPriceService


stocks = APIRouter(prefix='/api')


@stocks.get('/price/')
def get_today_price(symbol:str, date:date = date.today(), db:Session=Depends(get_db)):
    daily_price = DailyPriceService(db)
    
    data = daily_price.todays_price(symbol=symbol.upper(), date=date)
    return data