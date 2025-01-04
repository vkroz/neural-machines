from fastapi import FastAPI
from app.api import routes

app = FastAPI()

app.include_router(routes.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Python on Docker Sample API"}
