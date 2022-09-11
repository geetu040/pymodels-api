from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from pydantic import BaseModel
# importing models
from models.cat_and_dog.main import predict as cat_and_dog_predict


app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000/"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CatAndDog(BaseModel):
    resized_img_base64:str = None
    img_url:str = None

@app.get("/")
def index():
	return {"hello", "world"}

@app.post("/cat_and_dog")
def cat_and_dog_post(item: CatAndDog):
    return json.dumps(
        cat_and_dog_predict(item.resized_img_base64, item.img_url)
    );