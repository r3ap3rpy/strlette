from starlette.applications import Starlette
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.routing import Route
from starlette.responses import HTMLResponse

HTML_404_PAGE = ...
HTML_500_PAGE = ...

async def not_found(request: Request, exc: HTTPException):
    return HTMLResponse(content=HTML_404_PAGE, status_code = exc.status_code)

async def server_error(request: Request, exc: HTTPException):
    return HTMLResponse(content=HTML_500_PAGE, status_code = exc.status_code)

exception_handlers = {
    404: not_found,
    500: server_error
        }

async def home(request):
    return HTMLResponse('<h1>Welcome</h1>')

routes = [Route('/',home)]

app = Starlette(routes = routes, exception_handlers = exception_handlers)
