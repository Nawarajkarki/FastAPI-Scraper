from datetime import datetime
from sqlalchemy.orm import Session

from src.App.schemas import nepaliPaisa_schemas
from src.App.model import nepaliPaisa_models


class NepaliPaisaCrud():
    
    def __init__(self, db:Session):
        self.db = db
        
    def fetch_all_companies(self):
        return self.db.query(nepaliPaisa_models.Company).all()

    def fetch_company_by_id(self, id:int):
        return self.db.query(nepaliPaisa_models.Company).filter(nepaliPaisa_models.Company.id == id).first()
    
    def fetch_company_by_symbol(self, symbol:str):
        return self.db.query(nepaliPaisa_models.Company).filter(nepaliPaisa_models.Company.symbol == symbol).first()
    
    def fetch_company_by_name(self, name:str):
        return self.db.query(nepaliPaisa_models.Company).filter(nepaliPaisa_models.Company.name == name).first()
    
    
    def create_new_company(self, company:nepaliPaisa_schemas.CompanyInDB):
        new_company = nepaliPaisa_models.Company(**company.model_dump())
        self.db.add(new_company)
        self.db.commit()
        self.db.refresh(new_company)
        return new_company
    
    
    
    
    def fetch_sector_by_id(self, id:int):
        return self.db.query(nepaliPaisa_models.Sector).filter(nepaliPaisa_models.Sector.id == id).first()
    
    def fetch_sector_by_name(self, name:str):
        return self.db.query(nepaliPaisa_models.Sector).filter(nepaliPaisa_models.Sector.name == name).first()
    
    
    def create_sector(self, new_item : nepaliPaisa_schemas.SectorCreate):
        sector = nepaliPaisa_models.Sector(name = new_item.name)
        self.db.add(sector)
        self.db.commit()
        self.db.refresh(sector)
        return sector
    
    
    
    
    
    def fetch_stock_price_by_date(self, company_id:int, date:datetime):
        return (self.db.query(nepaliPaisa_models.DailyStockPrice).filter(
                    nepaliPaisa_models.DailyStockPrice.company_id == company_id,
                    nepaliPaisa_models.DailyStockPrice.date == date).first())
        
        
    def add_new_item(self, new_item:nepaliPaisa_schemas.DailyStockPriceCreate):
        new_data = nepaliPaisa_models.DailyStockPrice(**new_item.model_dump())
        self.db.add(new_data)
        self.db.commit()
        self.db.refresh(new_data)
        return new_data


        

    
    
    
    
    


        
    
    
    
    
    
        
