from fastapi.param_functions import Depends
import requests
from fastapi import APIRouter
from starlette.responses import RedirectResponse

from config import settings
from .middleware.middlewares import filter_data

router = APIRouter()


@router.post('/sendMessage')
def send_message(data: dict):
    r = requests.post(
        url=f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage',
        data={
            'text': data.get('text'),
            'chat_id': data.get('chat_id'),
        })

    return {
        'status': r.ok
    }


@router.get('/getFile')
def get_file(data: dict):
    r = requests.get(url=f'https://api.telegram.org/bot{settings.BOT_TOKEN}/getFile?file_id={data.get("file_id")}')
    return {
        'status': r.ok,
        'chat_id': data.get('chat_id'),
        'file_path': r.json().get('result').get('file_path')
    }


@router.get('/downloadFile')
def download_file(data: dict = Depends(filter_data)):
    r = requests.get(url=f'https://api.telegram.org/file/bot{settings.BOT_TOKEN}/{data.get("file_path")}')
    return {
        'status': r.ok,
        'chat_id': data.get('chat_id'),
        'file': r.raw
    }


@router.post('/sendPhoto')
def send_photo(data: dict = Depends(filter_data)):
    r = requests.post(
        url=f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendPhoto',
        data={
            'photo': data.get('file_id'),
            'chat_id': data.get('chat_id'),
        })

    return {
        'status': r.ok
    }