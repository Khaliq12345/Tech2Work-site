from sqlmodel import Session
from contextlib import contextmanager
from src.core.config import ENGINE
from src.core.config import SMTP_USERNAME, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT
import smtplib
import ssl
from email.message import EmailMessage


@contextmanager
def get_session():
    session = Session(ENGINE)
    try:
        yield session
    except Exception as e:
        print(f"DB error - {e}")
    finally:
        session.close()


def send_email_message(subject: str, content: str) -> dict:
    #
    message = EmailMessage()
    message["From"] = SMTP_USERNAME
    message["To"] = SMTP_USERNAME
    message["Subject"] = subject
    message.set_content(content)
    message.add_alternative(content, subtype="html")
    #
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(SMTP_SERVER, int(SMTP_PORT)) as server:
            server.starttls(context=context)
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(message)
        return {"status": "success", "message": "Email envoyé"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
