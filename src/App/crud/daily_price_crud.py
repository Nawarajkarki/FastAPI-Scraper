from sqlalchemy.orm import Session
from datetime import datetime

from src.App.schemas import schemas
from src.App.model import models
from .companyCrud import SectorCrud
from .companyCrud import CompanyCrud


class DailySharePriceCrud():
    
    def __init__(self, db:Session):
        self.db = db
        
        
    def fetch_stock_price_by_date(self, company_id:int, date:datetime):
        return (self.db.query(models.DailyStockPrice).filter(
                    models.DailyStockPrice.company_id == company_id,
                    models.DailyStockPrice.date == date).first())
        
        
        
    def add_new_item(self, new_item:schemas.DailyStockPriceCreate):
        new_data = models.DailyStockPrice(**new_item.model_dump())
        self.db.add(new_data)
        self.db.commit()
        self.db.refresh(new_data)
        return new_data
    
    
    
    
        
