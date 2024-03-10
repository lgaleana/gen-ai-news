import pytest
from fastapi.testclient import TestClient
from main import app

test_app = TestClient(app)

def test_read_root():
    response = test_app.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Welcome to our news application!'}

def test_get_news():
    response = test_app.get('/news')
    assert response.status_code == 200
    assert response.json() == {'message': 'News endpoint'}
