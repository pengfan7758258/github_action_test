import os
import sys

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/foods/{food_id}")
def read_food(food_id: int, q: str = None):
    return {"item_id": food_id, "q": q}


@app.get("/healthz")
async def health_check():
    return {"status": "ok"}
