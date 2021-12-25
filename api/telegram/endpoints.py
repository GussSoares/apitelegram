from fastapi import APIRouter, Depends

from api.middleware.middlewares import filter_data

from .telegram import Telegram

router = APIRouter()


@router.post("/sendMessage")
def send_message(data: dict = Depends(filter_data)):
    response = Telegram().send_message(data)
    return {"status": response.ok}


@router.post("/sendPhoto")
def send_photo(data: dict = Depends(filter_data)):
    response = Telegram().send_photo(data)
    return {"status": response.ok}
