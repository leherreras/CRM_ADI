import logging

from fastapi import FastAPI

import loggers
from app import routes

# Config the logging in the system
loggers.initialize_logging()

default_logger = logging.getLogger('uvicorn')

app = FastAPI()

# Register endpoints
routes.register(app)
