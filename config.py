from pydantic import SecretStr, BaseSettings
from exceptions import AccessError


class Settings(BaseSettings):
    access = False
    bot_token: SecretStr
    password: SecretStr
    db_file: SecretStr
    admin_id: SecretStr

    def __init__(self, password: str):
        super().__init__()
        print(self.access)
        self.match_password(password)

    def __getattribute__(self, name):
        possible = ('match_password', '_Settings__access', '_build_values', '__config__', '__fields__', '__dict__',
                    '__class__', '_init_private_attributes', '__private_attributes__', 'password', 'access')
        if name in possible:
            return object.__getattribute__(self, name)
        elif self.access:
            try:
                return object.__getattribute__(self, name).get_secret_value()
            except AttributeError:
                return object.__getattribute__(self, name)
        else:
            raise AccessError("you don't have acceess rights")

    def match_password(self, password: str):
        if self.password.get_secret_value() == password:
            self.access = True
        else:
            self.access = False
            raise AccessError("wrong password")

    class Config:
        env_file = 'data/config.env'
        env_file_encoding = 'utf-8'


config = Settings('12345')
