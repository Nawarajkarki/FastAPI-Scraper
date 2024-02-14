from sqlalchemy.orm import Session

from src.App.schemas import schemas
from src.App.model import models



class SectorCrud():
    
    def __init__(self, db:Session):
        self.db = db
        
        
    
    def fetch_sector_by_id(self, id:int):
        return self.db.query(models.Sector).filter(models.Sector.id == id).first()
    
    def fetch_sector_by_name(self, name:str):
        return self.db.query(models.Sector).filter(models.Sector.name == name).first()
    
    def create_sector(self, new_item : schemas.SectorCreate):
        sector = models.Sector(name = new_item.name)
        self.db.add(sector)
        self.db.commit()
        self.db.refresh(sector)
        return sector




class CompanyCrud():
    
    def __init__(self, db:Session):
        self.db = db
        
    
    def fetch_company_by_id(self, id:int):
        return self.db.query(models.Company).filter(models.Company.id == id).first()
    
    def fetch_company_by_symbol(self, symbol:str):
        return self.db.query(models.Company).filter(models.Company.symbol == symbol).first()
    
    def fetch_company_by_name(self, name:str):
        return self.db.query(models.Company).filter(models.Company.name == name).first()
    
    def create_new_company(self, company:schemas.CompanyInDB):
        new_company = models.Company(**company.model_dump())
        self.db.add(new_company)
        self.db.commit()
        self.db.refresh(new_company)
        return new_company