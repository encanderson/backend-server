from typing import List
from pydantic import AnyHttpUrl, BaseSettings
from fastapi_mail import ConnectionConfig
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    # List urls
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000"]
    PROJECT_NAME: str = "API - Register and Authentication"
    SERVER_NAME: str = os.getenv('SERVER_NAME')
    URL: str = os.getenv('URL')

    MONGO_DB_URL: str = os.getenv('MONGO_DB_URL')
    # POSTGRESQL_URL: str = os.getenv('POSTGRESQL_URI')
    # REDIS_HOST: str = 'localhost'

    MAIL_USER: str = os.getenv('EMAIL_USER')
    MAIL_PASSWORD: str = os.getenv('EMAIL_PASS')
    EMAIL_CONFIG = ConnectionConfig(
        MAIL_USERNAME=MAIL_USER,
        MAIL_PASSWORD=MAIL_PASSWORD,
        MAIL_FROM=MAIL_USER,
        MAIL_PORT=587,
        MAIL_SERVER=os.getenv('MAIL_SERVER'),
        MAIL_FROM_NAME='APP',
        MAIL_TLS=True,
        MAIL_SSL=False,
        USE_CREDENTIALS=True
    )

    class Config:
        case_sensitive = True


settings = Settings()
