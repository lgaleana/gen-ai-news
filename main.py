from fastapi import FastAPI
from gnews_api import fetch_news

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Welcome to our news application!'}

@app.get('/news')
def get_news():
    news = fetch_news('gen ai')
    return news
