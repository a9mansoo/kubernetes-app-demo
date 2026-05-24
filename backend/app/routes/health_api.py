from fastapi import APIRouter

health_api = APIRouter(tags=["healthcheck"])


@health_api.get("/ready")
async def ready_probe():
    return {"msg": "App is ready"}


@health_api.get("/live")
async def liveness_probe():
    return {"msg": "App is live"}
