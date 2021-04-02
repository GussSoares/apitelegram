from fastapi import APIRouter
import requests

from config import settings


router = APIRouter()

@router.post('/webhook')
def webhook(data: dict):
    r = requests.post(
        url=f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage',
        data={
            'text': data.get('message').get('text'),
            'chat_id': data.get('message').get('chat').get('id'),
        }
    )
    return {
        'status': r.ok
    }