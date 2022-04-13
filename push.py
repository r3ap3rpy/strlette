from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles

async def home(request):
    await request.send_push_promise("/static/style.css")
    return HTMLResponse('<html><head><link rel="stylesheet" href="/static/style.css"/></head></html>')

routes = [Route('/',home),Mount('/static',StaticFiles(directory="static"),name = 'static')]

app = Starlette(routes = routes)
