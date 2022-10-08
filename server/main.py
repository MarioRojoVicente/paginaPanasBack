from fastapi import FastAPI
from .routers import users, projects

app = FastAPI()


app.include_router(users.router)
app.include_router(projects.router)

@app.get("/ping")
async def ping():
    return {"message": "succesfull ping"}