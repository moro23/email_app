import os
from fastapi import BackgroundTasks 
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig 

from config.config import Settings

from dotenv import load_dotenv 
load_dotenv('.env')

class Email:
    def __init__(self):
        pass

    ## 
    conf = ConnectionConfig(
    MAIL_USERNAME= Settings.MAIL_USERNAME,
    MAIL_PASSWORD= Settings.MAIL_PASSWORD,
    MAIL_FROM= Settings.MAIL_FROM,
    MAIL_PORT= Settings.MAIL_PORT,
    MAIL_SERVER= Settings.MAIL_SERVER,
    MAIL_STARTTLS = Settings.MAIL_STARTTLS,
    MAIL_SSL_TLS = Settings.MAIL_SSL_TLS,
    MAIL_FROM_NAME= Settings.MAIL_FROM_NAME,
    USE_CREDENTIALS=True,
    TEMPLATE_FOLDER='./templates'

    )
    
    async def send_email_async(self, subject: str, email_to: str, body: dict):
        message = MessageSchema(
            subject=subject, 
            recipients=[email_to],
            body=body,
            subtype='html'
        )

        fm = FastMail(self.conf)
        await fm.send_message(message, template_name='email.html')


    def send_email_background(self, background_tasks: BackgroundTasks, subject: str, email_to: str, body: dict):
        message = MessageSchema(
            subject=subject,
            recipients=[email_to],
            body=body,
            subtype='html',
        )

        fm = FastMail(self.conf)
        background_tasks.add_task(fm.send_message, message, template_name='email.html')


