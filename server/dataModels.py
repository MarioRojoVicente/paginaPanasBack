from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    tags: list[str] | None = None

class Project(BaseModel):
    id: int
    name: str
    tags: list[str]
    participants: list[User]
    description: str
