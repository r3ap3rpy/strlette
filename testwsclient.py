from starlette.testclient import TestClient
from starlette.websockets import WebSocket

async def app(scope, receive, send):
    assert scope['type'] == 'websocket'
    websocket = WebSocket(scope, receive = receive, send = send)
    assert websocket.accept()
    assert websocket.send_text('Hello, world!')
    assert websocket.close()


def test_app():
    client = TestClient(app)
    with client.websocket_connect('/') as websocket:
        data = websocket.receive_text()
        assert data == 'Hello, world!'
