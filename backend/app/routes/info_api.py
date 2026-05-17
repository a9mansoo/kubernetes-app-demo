from fastapi import APIRouter, Request

info_api = APIRouter(tags=["info"])


@info_api.get("/version")
def get_app_version_info(request: Request):
    version = request.app.version
    return {"version": version}
