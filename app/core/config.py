from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Проект ЯП'
    app_description: str = 'Описание'
    database_url: str = (
        'postgresql+asyncpg://user:password@localhost:5432/mydatabase'
    )
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
