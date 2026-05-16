from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import health_api, user_api
from .config import Config


def add_middleware(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


def add_api_routes(app):
    app.include_router(health_api, prefix="/hlth")
    app.include_router(user_api, prefix="/user")
    return app


def create_app(app_config):
    app = FastAPI(
        title="FastAPI Backend Application",
        description="Backend application",
        summary="API endpoints",
        version="1.0.0",
        root_path=app_config.root_path,
    )
    app = add_api_routes(app)
    app = add_middleware(app)
    return app


def generate_app_config(**kwargs):
    config = Config(**kwargs)
    return config
