import requests
from fastapi import FastAPI

from router import router
from settings.config import settings

app = FastAPI()
app.include_router(router)


@app.get("/")
def startup():
    return {"status": "funciona"}
