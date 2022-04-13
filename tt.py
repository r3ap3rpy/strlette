from tartiflette import Resolver
from tartiflette_asgi import TartifletteApp

@Resolver("Query.hello")
async def hello(parent, args, context, info):
    name = args["name"]
    return f"Hello, {name}!"

sdl = "type Query { hello(name: String): String }"
app = TartifletteApp(sdl=sdl, path="/graphql")
