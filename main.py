from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None

@app.get("/")
def read_root():
    return {"message": "Welcome Misty to your first made API. This message is only for you. You will get $20 a week everytime you come here!"}

@app.post("/create-item/")
def create_item(item: Item):
    return {"name": item.name, "description": item.description}
