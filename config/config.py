import os

class Settings:
    MAIL_USERNAME: str = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD: str = os.getenv("MAIL_PASSWORD")
    MAIL_FROM: str = os.getenv("MAIL_FROM")
    MAIL_PORT: str = os.getenv("MAIL_PORT",)
    MAIL_SERVER: str = os.getenv("MAIL_SERVER")
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = os.getenv("MAIL_SSL_TLS", False)
    MAIL_FROM_NAME: str = os.getenv("MAIL_FROM_NAME")
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True

    class Config:
        env_file = './.env'

settings = Settings()

