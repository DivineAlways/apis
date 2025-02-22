from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None

@app.get("/")
def read_root():
    return {"watch this video": "https://youtu.be/LbAzTzlj3ac?si=q3A7bYccC3_sIjCl"}

@app.post("/create-item/")
def create_item(item: Item):
    return {"name": item.name, "description": item.description}
