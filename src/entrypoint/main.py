from fastapi import FastAPI

from src.entrypoint.database import test_db_connection
from src.App.router.nepalipaisa_router import stocks, scraper
from src.App.router.daraz_router import daraz, product

test_db_connection()

app = FastAPI()
app.include_router(scraper)
app.include_router(stocks)
app.include_router(daraz)
app.include_router(product)


@app.get('/')
def home():
    return "This is home!!.. . .  .   .     .  "