from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Mount, Route
from tartiflette import Resolver
from tartiflette_asgi import TartifletteApp

@Resolver("Query.hello")
async def hello(parent, args, context, info):
    name = args["name"]
    return f"Hello {name}"

sdl = "type Query { hello(name: String): String }"
graphql = TartifletteApp(sdl = sdl)

async def home(request):
    return PlainTextResponse("Hello Graphql!")

routes = [
    Route("/",endpoint = home),
    Mount("/graphql", graphql)
        ]

app = Starlette(routes = routes, on_startup = [graphql.startup])
