import requests
from fastapi import FastAPI

from settings.config import settings
from router import router

app = FastAPI()
app.include_router(router)


@app.get('/')
def startup():
    return {'status': 'funciona'}
