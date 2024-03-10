import os
import requests


def fetch_news(query):
    api_key = os.getenv('GNEWS_API_KEY')
    response = requests.get(f'https://gnews.io/api/v4/search?q={query}&token={api_key}')
    return response.json()
