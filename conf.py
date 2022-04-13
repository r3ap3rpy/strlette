import databases
//environment variables
// .env
//config
from starlette.applications import Starlette
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

config = Config('.env')

print(config("DATABASE_URL"))
