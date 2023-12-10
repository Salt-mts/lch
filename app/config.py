from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_host: str
    db_name: str
    db_user: str
    db_password: str
    db_port: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    mail_password: str

    

    class Config:
        env_file = ".env"



settings = Settings()