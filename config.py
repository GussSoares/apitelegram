from pydantic import BaseSettings


class Env(BaseSettings):
    BOT_TOKEN: str

    class Config:
        env_file = '.env'


settings = Env()