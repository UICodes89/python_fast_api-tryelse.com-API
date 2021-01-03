from fastapi import FastAPI
from typing import Optional
from enum import Enum

app = FastAPI()

fake_item_db = [
    {"item_name":"foo"},
    {"item_name":"Bar"}, 
    {"item_name":"Baz"},
    {"item_name":"Bar_foo"}, 
    {"item_name":"Baz_foo"},
    {"item_name":"Bar_g"}, 
    {"item_name":"Baz_ghww"},
    {"item_name":"Baz_ghss"},
    {"item_name":"Baz_ghs"},
    {"item_name":"Baz_ghf"}
]

@app.get("/")
async def root():
	return {"message":"Hello World"}

@app.get("/item/{main}")
async def root(main):
    return {"item_id":main}

@app.get("/user/id/{item_id}")
async def root(item_id: int):
    return {"item_id":item_id}

class ModelName(str, Enum):
	alexnet = "alexnet"
	resnet = "resnet"
	lenet = "lenet"

@app.get("/models/{model_name}")
async def root(model_name:ModelName):
    if model_name == ModelName.alexnet:
        return{"model_name": model_name,"message":"Deep Learining FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name,"message":"LeCNN all the images"}
    
    return {"model_name": model_name,"message":"Have someresiduals"}

@app.get("/items/")
async def root(skip:int = 0, limit:int =10):
    return fake_item_db[skip: limit]


#Optional Paremeter

@app.get('/items/{item_id}')
async def root(item_id:str, q: Optional[str] = None, short: bool= False):
    if q:
        return {"item_id":item_id, "q":q}
    if not short:
        return {"item_id":item_id, "short":short}
    return {"item_id":item_id}