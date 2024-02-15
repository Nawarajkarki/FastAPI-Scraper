from datetime import datetime

from fastapi import HTTPException
from sqlalchemy import inspect
from sqlalchemy.orm import Session

from src.App.crud.nepali_paisa_crud import NepaliPaisaCrud
from src.App.schemas import nepaliPaisa_schemas
from src.App.scrapers import nepaliPaisa_scraper









class ScrapeCompany:
    
    def __init__(self, db:Session):
        self.sector_crud = NepaliPaisaCrud(db)
        self.company_crud = NepaliPaisaCrud(db)

    
    def get_all_companies(self):
        companies = self.company_crud.fetch_all_companies()
        return companies
        
        
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
            # pass
        
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
    
    
    
    
    def create_company(self, company : nepaliPaisa_schemas.CompanyCreate):
        company_indb = self.company_crud.fetch_company_by_name(company.name)
        if company_indb is not None:
            return company_indb
            # raise HTTPException(status_code=401, detail="company with the given name already exist.")
        if company.sector is None:
            print('sector is none')
            sector_id = None
            
        else:
            print("sector not none\n\n\n\n\n\n")
            sector_indb = self.sector_crud.fetch_sector_by_name(company.sector)
            
            if sector_indb is None:
                sector_item = nepaliPaisa_schemas.SectorCreate(name=company.sector)
                add_sector = self.sector_crud.create_sector(sector_item)
                sector_id = add_sector.id
                
            elif sector_indb is not None:
                sector_id = sector_indb.id
        

        # company = schemas.CompanyInDB(**company.model_dump(), sector=sector_id)
        company_todb = nepaliPaisa_schemas.CompanyInDB(**company.model_dump(exclude={'sector'}), sector_id=sector_id if not None else None)
        
        company = self.company_crud.create_new_company(company_todb)
        print(f"compnay = {company.symbol}, \n\ncompnay_todb = {company_todb}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        return company
    
    
    
    
    
    
    
    def scrape_company_and_add_to_db(self):
        for company in nepaliPaisa_scraper.scrape_companies():
            self.create_company(company)
            print(f"the company is {company}")
            print('\n\n\n')
        return "Completed Adding companies"
    




class DailyPriceService():
    def __init__(self, db:Session):
        self.crud = NepaliPaisaCrud(db)
        self.company_crud = NepaliPaisaCrud(db)
        self.company_service = ScrapeCompany(db)
    
    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
    
    def todays_price(self, symbol:str, date:datetime):
        company_id = self.company_service.get_company_id(symbol=symbol)
        
        daily_stock_price = self.crud.fetch_stock_price_by_date(company_id=company_id, date=date)
        if daily_stock_price is None:
            raise HTTPException(status_code=401, detail="Price data for company of that date not found")
        
        # return daily_stock_price
        company = self.company_service.get_company_by_symbol(symbol=symbol)

 
        daily_stock_price_dict = {key: value for key, value in daily_stock_price.__dict__.items() if not key.startswith('_sa')}
        company_dict = {key: value for key, value in company.__dict__.items() if not key.startswith('_sa')}

        # Combine the dictionaries and return the result
        return {**daily_stock_price_dict, **company_dict}
        # return data.company
    
    
    
    
    
    def add_new_data(self, data:nepaliPaisa_schemas.DailyStockPriceCreate):
        company = self.company_crud.fetch_company_by_symbol(data.symbol)
        
        if company is None:
            '''Add a new column for that compnay.'''
            new_company = nepaliPaisa_schemas.CompanyCreate(
                name = data.name,
                symbol = data.symbol,
                sector = None
            )
            company_data = self.company_service.create_company(company=new_company)
            company_id = company_data.id
            # raise HTTPException(status_code=404, detail={"msg" : "Company wasn't found in the company table", "Data" : data})
        
        else:
            company_id = company.id
        
        new_data = nepaliPaisa_schemas.DailyStockPriceInDb(**data.model_dump(), company_id=company_id)   
        
        todays_price = self.crud.fetch_stock_price_by_date(company_id = company_id, date=new_data.date)
        if todays_price is None:
            self.crud.add_new_item(new_data)
            return True     
        
        
    
    
    def daily_share_price(self):
        for stock in nepaliPaisa_scraper.today_share_price_scraper():
            self.add_new_data(stock)


