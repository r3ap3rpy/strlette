from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response
from starlette.routing import Route

async def home(request):
    return Response('Hello World!', media_type = 'text/plain')

routes = [
    Route('/',home)
        ]

middleware = [
    Middleware(CORSMiddleware, allow_origins = ['*']),
        ]

app = Starlette(routes = routes, middleware = middleware)
