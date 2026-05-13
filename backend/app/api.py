from fastapi import APIRouter


health_check = APIRouter(tags=["healthcheck"])


@health_check.get("/ready")
def ready_probe():
    return "App is ready"


@health_check.get("/live")
def liveness_probe():
    return "App is live"


@health_check.get("/ok")
def ok():
    return {"user": "fakename"}
