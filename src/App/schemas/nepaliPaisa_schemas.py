from pydantic import BaseModel
from datetime import date



class SectorCreate(BaseModel):
    name : str

class Sector(SectorCreate):
    id : int
    

class CompanyBase(BaseModel):
    name : str
    symbol : str
    
class CompanyCreate(CompanyBase):
    sector : str | None = None
    pass

class Company(CompanyBase):
    id : int

class CompanyInDB(CompanyBase):
    sector_id : int | None = None
    
    
    
    
class DailyStockPriceBase(BaseModel):
    openPrice : float
    closePrice : float
    highPrice : float
    lowPrice : float
    previousClose : float
    volume : int
    date : date


class DailyStockPriceCreate(DailyStockPriceBase):
    symbol : str
    name: str 
    
    
class DailyStockPriceInDb(DailyStockPriceBase):
    company_id : int
    
