import server.crud.users as Crud 
from fastapi import APIRouter
from ..dataModels import User

router = APIRouter(
    prefix="/users",
    tags=["users"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/{user_id}")
async def get_user_by_id(user_id):
    return Crud.get_user_by_id(user_id)

@router.get("/list")
async def get_users_list():
    return Crud.get_users_list()
