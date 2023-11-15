from pydantic import BaseSettings, SecretStr
from exceptions import AccessError


class Settings(BaseSettings):
    __access = False
    bot_token: SecretStr
    __password: SecretStr
    db_file: SecretStr

    def __getattribute__(self, name):
        if self.__access:
            return object.__getattribute__(self, name)
        else:
            raise AccessError("you don't have acceess rights")

    def match_password(self, password: str):
        if self.__password.get_secret_value() == password:
            self.__access = True
        else:
            self.__access = False
            raise AccessError("wrong password")

    class Config:
        env_file = 'data/config.env'
        env_file_encoding = 'utf-8'


config = Settings()
