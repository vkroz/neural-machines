from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
async def hello():
    return {"message": "Hello, World!"}

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
