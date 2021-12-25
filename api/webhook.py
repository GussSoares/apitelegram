from fastapi import APIRouter, Depends

from api.telegram.telegram import Telegram

from .middleware.middlewares import filter_data

router = APIRouter()


@router.post("/webhook")
def webhook(data: dict = Depends(filter_data)):
    # return RedirectResponse(url=data.get('url'), status_code=status.HTTP_307_TEMPORARY_REDIRECT)
    if data.get("type") == "sendMessage":
        response = Telegram().send_message(data)
    elif data.get("type") == "sendPhoto":
        response = Telegram().send_photo(data)
    else:
        response = Telegram().send_message(data)

    return {
        'status': response.ok
    }
