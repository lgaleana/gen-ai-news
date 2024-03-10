import requests


def fetch_news(query):
    response = requests.get(f'https://gnews.io/api/v4/search?q={query}&token=API_KEY')
    return response.json()
