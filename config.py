from pydantic import BaseSettings


class Env(BaseSettings):
    BOT_TOKEN: str
    BOT_MY_CHAT_ID: str
    class Config:
        env_file = '.env'


settings = Env()