from fastapi import APIRouter

health_api = APIRouter(tags=["healthcheck"])


@health_api.get("/ready")
async def ready_probe():
    return "App is ready"


@health_api.get("/live")
async def liveness_probe():
    return "App is live"
