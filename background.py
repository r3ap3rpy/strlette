from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route
from starlette.background import BackgroundTasks


async def home(request):
    tasks = BackgroundTasks()
    tasks.add_task(task_one)
    tasks.add_task(task_two)
    return PlainTextResponse("Background tasks!")


async def task_one():
    print("Executing task one!")

async def task_two():
    print("Executing task two!")

routes = [Route('/',home)]

app = Starlette(routes = routes)
