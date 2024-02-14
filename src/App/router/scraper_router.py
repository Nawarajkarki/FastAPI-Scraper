from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from src.entrypoint.database import get_db
from src.App.services.scrape import ScrapeCompany, DailyPriceService

scraper = APIRouter(prefix='/api/scraper', tags=['Scraper'])


@scraper.get('/company')
def scrape(db:Session=Depends(get_db)):
    scraper = ScrapeCompany(db)
    scraper.scrape_company_and_add_to_db()
    return "scraped"
    
    
@scraper.get('/dailyPrice')
def scrape(db:Session=Depends(get_db)):
    scraper = DailyPriceService(db)
    scraper.daily_share_price()
    return "scraped"



