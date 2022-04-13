from starlette.responses import HTMLResponse
from starlette.testclient import TestClient

async def app(scope, receive, send):
    assert scope['type'] == 'http'
    response = HTMLResponse('<h1>Welcomme</h1>')
    await response(scope, receive, send)

def test_app():
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == 200
