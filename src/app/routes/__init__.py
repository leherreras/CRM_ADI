from fastapi import FastAPI

from app.routes.lead import router_lead
from app.routes.prospect import router_prospect


def register(app: FastAPI):
    """Register all the routers in app."""
    app.include_router(router_lead, prefix="/lead")
    app.include_router(router_prospect, prefix="/prospect")
