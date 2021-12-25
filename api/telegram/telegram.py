import requests
from fastapi.param_functions import Depends

from api.middleware.middlewares import filter_data
from settings.config import settings


class Telegram(object):
    def __init__(self) -> None:
        super().__init__()
        self.request = requests

    def send_message(self, data: dict = Depends(filter_data)):
        return self.request.post(
            url=f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage",
            data={
                "text": data.get("text"),
                "chat_id": data.get("chat_id"),
            },
        )

    def send_photo(self, data: dict = Depends(filter_data)):
        return self.request.post(
            url=f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendPhoto",
            data={
                "photo": data.get("file_id"),
                "chat_id": data.get("chat_id"),
            },
        )

    def get_file(self, data: dict):
        r = self.request.get(
            url=f'https://api.telegram.org/bot{settings.BOT_TOKEN}/getFile?file_id={data.get("file_id")}'
        )
        return {
            "status": r.ok,
            "chat_id": data.get("chat_id"),
            "file_path": r.json().get("result").get("file_path"),
        }

    def download_file(self, data: dict = Depends(filter_data)):
        r = self.request.get(
            url=f'https://api.telegram.org/file/bot{settings.BOT_TOKEN}/{data.get("file_path")}'
        )
        return {"status": r.ok, "chat_id": data.get("chat_id"), "file": r.raw}
