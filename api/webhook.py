from fastapi import APIRouter, Depends, status
from starlette.responses import RedirectResponse

from .middleware.middlewares import filter_data
from api.telegram.telegram import Telegram


router = APIRouter()

@router.post('/webhook')
def webhook(data: dict = Depends(filter_data)):
    # return RedirectResponse(url=data.get('url'), status_code=status.HTTP_307_TEMPORARY_REDIRECT)
    if data.get('type') == 'sendMessage':
        response = Telegram().send_message(data)
    elif data.get('type') == 'sendPhoto':
        response = Telegram().send_photo(data)
    
    return {
        'status': response.ok
    }