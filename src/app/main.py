import logging

from fastapi import FastAPI

import loggers
from app import routes

loggers.initialize_logging()

default_logger = logging.getLogger('uvicorn')

app = FastAPI()

routes.register(app)
