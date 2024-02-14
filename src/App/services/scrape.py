from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.App.crud.companyCrud import SectorCrud, CompanyCrud
from src.App.schemas import schemas
from src.App.model import models



from src.App.scrapers import nepaliPaisa









class ScrapeCompany:
    
    def __init__(self, db:Session):
        self.sector_crud = SectorCrud(db)
        self.company_crud = CompanyCrud(db)
        
        
    def get_company_id(self, symbol:str=None, name:str=None):
        if symbol is not None:
            company = self.get_company_by_symbol(symbol=symbol)
            print(f"the company id is {company.id}")
            return company.id
        if name is not None:
            company = self.get_company_by_name(name=name)
            return company.id
        
        
    def get_company_by_id(self, id:int):
        company = self.company_crud.fetch_company_by_id(id)
        if company is None:
            raise HTTPException(status_code=401, detail="Invalid Company ID")
        return company
    
    
    def get_company_by_symbol(self, symbol:str):
        company = self.company_crud.fetch_company_by_symbol(symbol)
        if company is None:
            raise HTTPException(status_code=401, detail="Invalid Company Symbol.")
        return company
    
    
    
    
    def get_company_by_name(self, name:str):
        company = self.company_crud.fetch_company_by_name(name)
        if company is None:
            raise HTTPException(status_code=401, detail="Invalid Company Name.")
        return company
    
    
    
    def get_sector_by_name(self, name:str):
        sector = self.sector_crud.fetch_sector_by_name(name)
        if sector is None:
            raise HTTPException(status_code=401, detail="Invalid sector Name.")
        return sector
    
    
    
    
    def create_company(self, company : schemas.CompanyCreate):
        company_indb = self.company_crud.fetch_company_by_name(company.name)
        if company_indb is not None:
            raise HTTPException(status_code=401, detail="company with the given name already exist.")
        
        sector_indb = self.sector_crud.fetch_sector_by_name(company.sector)
        
        if sector_indb is None:
            sector_item = schemas.SectorCreate(name=company.sector)
            add_sector = self.sector_crud.create_sector(sector_item)
            sector_id = add_sector.id
            
        elif sector_indb is not None:
            sector_id = sector_indb.id
            
        # company = schemas.CompanyInDB(**company.model_dump(), sector=sector_id)
        company = schemas.CompanyInDB(**company.model_dump(exclude={'sector'}), sector_id=sector_id)
        
        return self.company_crud.create_new_company(company)
    
    
    
    
    
    
    
    def scrape_company_and_add_to_db(self):
        for company in nepaliPaisa.scrape_companies():
            self.create_company(company)
            print(f"the company is {company}")
            print('\n\n\n')
        return "Completed Adding companies"
    

from datetime import datetime
from src.App.crud.daily_price_crud import DailySharePriceCrud

class DailyPriceService():
    def __init__(self, db:Session):
        self.crud = DailySharePriceCrud(db)
        self.company_crud = CompanyCrud(db)
        self.company_service = ScrapeCompany(db)
    
    
    
    def todays_price(self, symbol:str, date:datetime):
        company_id = self.company_service.get_company_id(symbol=symbol)
        
        daily_stock_price = self.crud.fetch_stock_price_by_date(company_id=company_id, date=date)
        if daily_stock_price is None:
            raise HTTPException(status_code=401, detail="Bad Fucking Request")
        
        # return daily_stock_price
        company = self.company_service.get_company_by_symbol(symbol=symbol)

 
        daily_stock_price_dict = {key: value for key, value in daily_stock_price.__dict__.items() if not key.startswith('_sa')}
        company_dict = {key: value for key, value in company.__dict__.items() if not key.startswith('_sa')}

        # Combine the dictionaries and return the result
        return {**daily_stock_price_dict, **company_dict}
        # return data.company
    
    
    
    
    
    def add_new_data(self, data:schemas.DailyStockPriceCreate):
        company = self.company_crud.fetch_company_by_symbol(data.symbol)
        
        if company is None:
            raise HTTPException(status_code=404, detail={"msg" : "Company wasn't found in the company table", "Data" : data})
        
        company_id = company.id
        new_data = schemas.DailyStockPriceInDb(**data.model_dump(), company_id=company_id)   
        
        todays_price = self.crud.fetch_stock_price_by_date(company_id = company_id, date=new_data.date)
        if todays_price is None:
            self.crud.add_new_item(new_data)
            return True     
    
    
    
    def daily_share_price(self):
        for stock in nepaliPaisa.today_share_price_scraper():
            self.add_new_data(stock)


