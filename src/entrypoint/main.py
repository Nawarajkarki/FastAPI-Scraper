from fastapi import FastAPI

from src.entrypoint.database import test_db_connection
from src.App.router.scraper_router import scraper
from src.App.router.router import stocks

test_db_connection()

app = FastAPI()
app.include_router(scraper)
app.include_router(stocks)


@app.get('/')
def home():
    return "This is home!!.. . .  .   .     .  "