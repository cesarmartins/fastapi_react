from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    email: str

database = []

@app.post("/items/")
async def create_item(item: Item):
    database.append(item.dict())
    return item
