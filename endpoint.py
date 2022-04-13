from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.endpoints import HTTPEndpoint
from starlette.routing import Route

class Homepage(HTTPEndpoint):
    async def get(self, request):
        return PlainTextResponse('Welcome to HTTPEndpoint class!')

class User(HTTPEndpoint):
    async def get(self, request):
        username = request.path_params['username']
        return PlainTextResponse(f'Welcome: {username}')

routes = [
    Route('/',Homepage),
    Route('/users/{username}',User),
        ]

app = Starlette(routes = routes)
