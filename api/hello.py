from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class ModelName(str, Enum):
    what = "what"
    where = "where"
    when = "when"

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

@app.get("/info/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.what:
        return {
            "model_name": model_name, 
            "message": "python api written with FastApi!"
        }

    if model_name == ModelName.when:
        return {"model_name": model_name, "message": "kiced things of about 9pm 11/05/2022"}

    return {"model_name": model_name, "message": "Running in kubernetties in GPC"}