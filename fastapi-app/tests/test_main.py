import pytest
from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch

test_app = TestClient(app)


def test_read_root():
    response = test_app.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Welcome to our news application!'}

@patch('main.fetch_news')
def test_get_news(mock_fetch):
    mock_fetch.return_value = [{'title': 'Test Article', 'description': 'Test Description', 'publishedAt': '2022-01-01', 'source': {'name': 'Test Source', 'url': 'https://test.com'}, 'url': 'https://test.com/article'}]
    response = test_app.get('/news')
    assert response.status_code == 200
    assert 'Test Article' in response.text
    assert 'Test Description' in response.text
    assert '2022-01-01' in response.text
    assert 'Test Source' in response.text
    assert 'https://test.com' in response.text
