from starlette.responses import PlainTextResponse

async def application(scope, receive, send):
    assert scope['type'] == 'http'
    response = PlainTextResponse('Welcome to starlette')
    await response(scope, receive, send)
