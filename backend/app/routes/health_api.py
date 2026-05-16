from fastapi import APIRouter


health_api = APIRouter(tags=["healthcheck"])


@health_api.get("/ready")
def ready_probe():
    return "App is ready"


@health_api.get("/live")
def liveness_probe():
    return "App is live"
