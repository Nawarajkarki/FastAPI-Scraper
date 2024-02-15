from sqlalchemy import func
from sqlalchemy.orm import Session


from src.App.schemas import daraz_schemas
from src.App.model import daraz_models

class DarazCrud():
    
    def __init__(self, db:Session):
        self.db = db
        
    
    # def fetch_item_by_keyword(self, keyword:str):
    #     items = self.db.query(daraz_models.DarazProducts).filter(
    #         daraz_models.DarazProducts.productName == keyword).all()
    #     return items
    
 
    def fetch_item_by_keyword(self, keyword:str):
        items = self.db.query(daraz_models.DarazProducts).filter(
            func.lower(daraz_models.DarazProducts.productName).like(f"%{keyword.lower()}%")).all()
        return items


    
    def fetch_item_by_url(self, url:str):
        item = self.db.query(daraz_models.DarazProducts).filter(
            daraz_models.DarazProducts.url == url).first()
        return item
    

        
    
        
    def add_new_item(self, data:daraz_schemas.DarazProductCreate):
        item = daraz_models.DarazProducts(**data.model_dump())
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item
    
    