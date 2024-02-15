import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from src.entrypoint.database import Base



class Sector(Base):
    __tablename__ = "sector"
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, unique=True, index=True)
    name = sa.Column(sa.VARCHAR(255), unique=True, nullable=False)
    
    
    # companies = relationship('Company', back_populates='sector')


class Company(Base):
    __tablename__ = "company"

    id = sa.Column(sa.INTEGER, primary_key=True, autoincrement=True, unique=True, index=True)
    name = sa.Column(sa.VARCHAR(255), nullable=False, index=True, unique=True)
    symbol = sa.Column(sa.VARCHAR(20), nullable=False, index=True, unique=True)
    sector_id = sa.Column(sa.INTEGER, sa.ForeignKey('sector.id'))
    
    # sector = relationship('Sector', back_populates='companies')
    daily_stock_prices = relationship('DailyStockPrice' ,back_populates='company')



class ShareTypes(Base):
    __tablename__ = "shareTypes"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, unique=True)
    name = sa.Column(sa.VARCHAR(55), unique=True)
    
    


class Ipo(Base):
    __tablename__ = "ipo"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, unique=True)
    companyName = sa.Column(sa.VARCHAR(255), nullable=False)
    symbol = sa.Column(sa.VARCHAR(20), nullable=False)
    sector_id = sa.Column(sa.Integer, sa.ForeignKey('sector.id'))
    shareType_id = sa.Column(sa.Integer, sa.ForeignKey('shareTypes.id'))
    totalUnits = sa.Column(sa.Integer, nullable=False)
    pricePerUnit = sa.Column(sa.Float, nullable=False)
    minUnits = sa.Column(sa.Integer, nullable=False)
    maxUnits = sa.Column(sa.Integer, nullable=False)
    ratings = sa.Column(sa.VARCHAR(50))
    openingDate = sa.Column(sa.Date, nullable=False)
    closingDate = sa.Column(sa.Date, nullable=False)
    staus = sa.Column(sa.Boolean)
    
    
    # sector = relationship('Sector', back_populates='ipos')
    # shareType = relationship('ShareTypes', back_populates='ipos')
    
    


class DailyStockPrice(Base):
    __tablename__ = "daily_stock_price"
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False)
    company_id = sa.Column(sa.Integer, sa.ForeignKey('company.id'), nullable=False)
    date = sa.Column(sa.Date, nullable=False)
    openPrice = sa.Column(sa.Float)
    closePrice = sa.Column(sa.Float)
    highPrice = sa.Column(sa.Float)
    lowPrice = sa.Column(sa.Float)
    previousClose = sa.Column(sa.Float)
    volume = sa.Column(sa.Integer)
    
    company = relationship('Company',uselist=False , back_populates='daily_stock_prices')
