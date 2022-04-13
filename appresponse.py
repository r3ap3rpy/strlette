from starlette.responses import Response, HTMLResponse, JSONResponse
from starlette.responses import PlainTextResponse, RedirectResponse
from starlette.responses import StreamingResponse
import asyncio

async def app(scope, receive, send):
    assert scope['type'] == 'http'
    response = Response('Hello World!', media_type = 'text/plain')
    await response(scope,receive, send)


async def app_html(scope, receive, send):
    assert scope['type'] == 'http'
    response = HTMLResponse('<h1>Hello HTML</h/h11>')
    await response(scope,receive, send)

async def app_json(scope, receive, send):
    assert scope['type'] == 'http'
    response = JSONResponse({'hello':'world'})
    await response(scope,receive, send)

async def app_redirect(scope, receive, send):
    assert scope['type'] == 'http'
    if scope['path'] !=  '/':
        response = RedirectResponse(url='/')
    else:
        response = PlainTextResponse('Hello World')
    await response(scope,receive, send)

async def slow_moth(minimum, maximum):
    yield('<html><body><ul>')
    for n in range(minimum, maximum + 1):
        yield(f'<li>{n}</li>')
        await asyncio.sleep(0.5)
    yield('</ul></body></html>')

async def app_streaming(scope, receive, send):
    assert scope['type'] == 'http'
    generator = slow_moth(1,10)
    response = StreamingResponse(generator, media_type = 'text/html')
    await response(scope,receive,send)

