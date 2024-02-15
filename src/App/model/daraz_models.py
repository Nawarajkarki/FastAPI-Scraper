import sqlalchemy as sa

from src.entrypoint.database import Base





class DarazProducts(Base):
    __tablename__ =  "daraz_products"
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False)
    productName = sa.Column(sa.VARCHAR(255), nullable=False, index=True)
    price = sa.Column(sa.FLOAT, nullable=False, index=True)
    free_delivery = sa.Column(sa.Boolean, default=False)
    ratings = sa.Column(sa.Float)
    num_of_ratings = sa.Column(sa.Float)
    total_sold = sa.Column(sa.Integer, default=0)
    url = sa.Column(sa.VARCHAR(500))
        