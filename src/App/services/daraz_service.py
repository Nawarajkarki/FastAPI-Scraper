from sqlalchemy.orm import Session
from fastapi import HTTPException


from src.App.crud.daraz_crud import DarazCrud
from src.App.schemas import daraz_schemas

from src.App.scrapers import daraz_scraper


class DarazService():
    def __init__(self, db:Session):
        self.crud = DarazCrud(db)    
    
    
    def get_all_items_by_keyword(self, keyword:str):
        items = self.crud.fetch_item_by_keyword(keyword)
        if not items :
            self.scrape_daraz_for_query(keyword)
            items = self.get_all_items_by_keyword(keyword)
        return items
        
    
    
    
    def add_new_item(self, data:daraz_schemas.DarazProductCreate):
        item = self.crud.fetch_item_by_url(data.url)
        if item is not None:
            raise HTTPException(status_code=402, detail='Item already in DB')
        
        new_item = self.crud.add_new_item(data)
        return new_item
    
    
    
    def scrape_daraz_for_query(self, query:str):
        for item in daraz_scraper.main(query):
            try:
                self.add_new_item(item)
            except HTTPException:
                print(f"This item is already in DB \n {item}")
                continue
            
        return True