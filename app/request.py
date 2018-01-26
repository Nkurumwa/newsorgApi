from app import app
from urllib import.request,json
from models import news

news = news.News

#getting api key

api_key = app.config["NEWS_API_KEY"]

#getting the news url

base_url = app.config["BOOK_API_BASE_URL"]