from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route, Mount, WebSocketRoute
from starlette.staticfiles import StaticFiles

def homepage(request):
    return PlainTextResponse('Welcome to application class!')

def user_me(request):
    username = "Daniel"
    return PlainTextResponse(f"Welcome {username}")

def user(request):
    username = request.path_params['username']
    return PlainTextResponse(f"Welcome user: {username}")

async def websocket_endpoint(websocket):
    assert websocket.accept()
    assert websocket.send_text('Hello websocket!')
    assert websocket.close()

def startup():
    print("Booting up the engine!")

routes = [
    Route('/',homepage),
    Route('/user/me',user_me),
    Route('/user/{username}',user),
    WebSocketRoute("/ws",websocket_endpoint),
    Mount('/static',StaticFiles(directory="static")),
        ]
app = Starlette(debug=True, routes = routes, on_startup = [startup])

