from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route

async def home(request):
    return PlainTextResponse('Welcome home!')

async def about(request):
    return PlainTextResponse("This is the about page!")

async def users(request):
    username = request.path_params['username']
    return PlainTextResponse(f'The specified username: {username}')

routes = [
    Route("/",endpoint=home),
    Route("/about",endpoint=about,methods=['GET']),
    Route("/users/{username}",endpoint=users),
        ]

#url = request.url_for('home')

app = Starlette(routes=routes)
