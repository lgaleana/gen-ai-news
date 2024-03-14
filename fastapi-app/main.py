from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
from jinja2 import Template
from gnews_api import fetch_news

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Welcome to our news application!'}

@app.get('/news', response_class=HTMLResponse)
def get_news():
    news = fetch_news('gen ai')
    with open('templates/news.html') as file_:
        template = Template(file_.read())
    return template.render(articles=news)
