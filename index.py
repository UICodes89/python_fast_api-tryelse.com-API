from fastapi import FastAPI
from enum import Enum

app = FastAPI()

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