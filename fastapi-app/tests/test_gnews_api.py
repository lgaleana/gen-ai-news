import pytest
from unittest.mock import patch
from gnews_api import fetch_news

@patch('requests.get')
def test_fetch_news(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'articles': [{'title': 'Test Article'}] * 20}
    articles = fetch_news('gen ai')
    assert len(articles) == 10
    assert articles[0] == {'title': 'Test Article'}

@patch('requests.get')
def test_fetch_news_failed(mock_get):
    mock_get.return_value.status_code = 400
    with pytest.raises(Exception):
        fetch_news('gen ai')