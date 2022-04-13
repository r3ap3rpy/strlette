from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import PlainTextResponse
async def startup():
    print("Application is booting up!")

async def shutdown():
    print("Application is shutting down!")

async def home(request):
    return PlainTextResponse("Event demo")

routes = [
    Route("/",home)
        ]

app = Starlette(routes = routes, on_startup = [startup],on_shutdown=[shutdown])
