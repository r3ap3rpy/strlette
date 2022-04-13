from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles
from starlette.responses import Response
from starlette.routing import Route

async def home(request):
    return Response('Hello World!', media_type = 'text/plain')

routes = [
    Route('/',home),
    Mount('/static',app = StaticFiles(directory='static'),name = 'static')
        ]

app = Starlette(routes = routes)

