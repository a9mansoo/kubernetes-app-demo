from fastapi import APIRouter


user_api = APIRouter(tags=["user"])

@user_api.get("/{id}")
def get_user_details(id: int):
    return {"user": "fakename", "id": id}
