from fastapi import APIRouter
from ..dataModels import Project

router = APIRouter(
    prefix="/projects",
    tags=["projects"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/{project_id}")
async def get_project_by_id():
    return 200

@router.get("/list")
async def get_projects_list( participant: str = None, category: str = None):
    return 200
