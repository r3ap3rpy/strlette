from events import app
from starlette.testclient import TestClient

def test_homepage():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
