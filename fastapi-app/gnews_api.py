from dotenv import load_dotenv
import os
import requests

load_dotenv()

def fetch_news(query):
    api_key = os.getenv('GNEWS_API_KEY')
    response = requests.get(f'https://gnews.io/api/v4/search?q={query}&token={api_key}')
    if response.status_code != 200:
        raise Exception('Failed to fetch news')
    data = response.json()
    articles = data.get('articles', [])[:10]
    return articles