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
    mock_fetch.return_value = {'articles': [{'title': 'Test Article'}]}
    response = test_app.get('/news')
    assert response.status_code == 200
    assert response.json() == {'articles': [{'title': 'Test Article'}]}
