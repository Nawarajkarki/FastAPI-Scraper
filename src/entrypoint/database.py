from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



SQLALCHEMY_URL = "postgresql://postgres:nope@localhost:5432/scraper"


engine = create_engine(SQLALCHEMY_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()
        



def test_db_connection():
    try:
        db = SessionLocal()
        result = db.execute(text("SELECT 1"))
        print(result.scalar())
        db.close()
        print("Connection to DataBase successfull")
    except Exception as e:
        print("DB Connection failed:", e)
        
