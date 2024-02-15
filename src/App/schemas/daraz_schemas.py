from pydantic import BaseModel




class DarazProductBase(BaseModel):
    productName : str
    price : float
    free_delivery : bool
    ratings : float | None = None
    num_of_ratings : float | None = None
    total_sold : int | None = None
    url : str
    
class DarazProductCreate(DarazProductBase):
    pass


class DarazProducts(DarazProductCreate):
    id : int
    
        

