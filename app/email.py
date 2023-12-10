from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from .config import settings
from .utils import baseURL


# conf = ConnectionConfig(
#     MAIL_USERNAME = 'noreply@labourch.com',
#     MAIL_PASSWORD = 'l0KOwoJvZrVL',
#     MAIL_FROM = "noreply@labourch.com",
#     MAIL_PORT = 465,
#     MAIL_SERVER = 'labourch.com',
#     MAIL_STARTTLS = True,
#     MAIL_SSL_TLS = False,
#     USE_CREDENTIALS = True,
#     TEMPLATE_FOLDER = 'templates',
# )

conf = ConnectionConfig(
    MAIL_USERNAME = 'mo6014245571@gmail.com',
    MAIL_PASSWORD = 'lnuu meou kcvs nhyk',
    MAIL_FROM = "mo6014245571@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_FROM_NAME = "Labour Connect Hub",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    TEMPLATE_FOLDER = 'templates',
)



async def welcome_email(subject: str, recipients: str, body: dict) -> JSONResponse:
    message = MessageSchema(
        subject=subject,
        recipients=[recipients],
        template_body=body,
        subtype='html',
        )

    fm = FastMail(conf)
    await fm.send_message(message, template_name="welcome_email.html") 



async def pass_reset_email(subject: str, recipients: str, body: dict) -> JSONResponse:
    message = MessageSchema(
        subject=subject,
        recipients=[recipients],
        template_body=body,
        subtype='html',
        )

    fm = FastMail(conf)
    await fm.send_message(message, template_name="pass_reset_email.html") 