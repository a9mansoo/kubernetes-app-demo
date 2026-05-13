from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import health_check


def add_middleware(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_methods=["*"],
        allow_headers=["*"]
    )
    return app


def add_api_routes(app):
    app.include_router(health_check, prefix="/hlth")
    return app

def create_app(app_config=None):
    app = FastAPI(title="FastAPI Backend Application", description="Backend application", summary="API endpoints", version="1.0.0", root_path="/api/v1/")
    app = add_api_routes(app)
    app = add_middleware(app)
    return app


