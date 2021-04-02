import requests
from fastapi import FastAPI

from config import settings


app = FastAPI()


@app.on_event('startup')
def startup():
    print('iniciou')


@app.get('/')
def startup():
    return {'status': 'funciona'}


@app.post('/sendMessage')
def send_message(data: dict):
    r = requests.post(
        url=f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage',
        data={
            'text': data.get('message'),
            'chat_id': data.get('chat_id'),
        })

    return {
        'status': r.ok
    }

