from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

templates = Jinja2Templates(directory='templates')

async def home(request):
    return templates.TemplateResponse('index.html',{'request':request})

routes = [
    Route('/',home),
    Mount('/static', StaticFiles(directory='static'), name = 'static')
    ]

app = Starlette(routes = routes, debug = True)
