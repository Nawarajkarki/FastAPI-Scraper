from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session


from src.entrypoint.database import get_db
from src.App.services.daraz_service import DarazService
from src.App.schemas import daraz_schemas



daraz = APIRouter(prefix='/api/scraper/daraz', tags=['Daraz', 'Daraz Scarper'])
product = APIRouter(prefix='/api/products', tags=['Daraz', 'Daraz Products'])

@daraz.get('/')
def scrape_specific_query(query:str, db:Session=Depends(get_db)):
    drz_scraper_service = DarazService(db)
    scraper = drz_scraper_service.scrape_daraz_for_query(query)
    
    return JSONResponse(
        status_code=202,
        content=f"Daraz first search resuld page for --  {query} --- scraped"
    )







@product.get('/', response_model=list[daraz_schemas.DarazProducts])
def get_items_by_keyword(keyword:str, db:Session=Depends(get_db)):
    drz_scraper_service = DarazService(db)
    items = drz_scraper_service.get_all_items_by_keyword(keyword)
    return items


