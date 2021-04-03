import requests
from fastapi import APIRouter, status, Depends
from starlette.responses import RedirectResponse

from config import settings
from .middleware.middlewares import filter_data


router = APIRouter()

@router.post('/webhook')
def webhook(data: dict = Depends(filter_data)):
    return RedirectResponse(url=data.get('url'))

    # r = requests.post(
    #     url=f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage',
    #     data={
    #         # 'text': data.get('message').get('text'),
    #         'text': str(data),
    #         'chat_id': data.get('message').get('chat').get('id'),
    #     }
    # )
    # return {
    #     'status': r.ok
    # }