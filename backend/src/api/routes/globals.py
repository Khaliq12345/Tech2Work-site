from typing import List
from fastapi import APIRouter
from sqlmodel import select
from src.models.global_models import create_table, ServiceTechStack, FAQ
from src.utils import get_session
from src.core.config import SMTP_USERNAME, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT
import smtplib
import ssl
from email.message import EmailMessage

route = APIRouter(prefix="/global")
route.add_event_handler("startup", create_table)


@route.get("/add-service-tech-stack")
def add_service_tech_stack(
    classname: str, title: str, desc: str, icon: str, type: str
):
    with get_session() as session:
        item = ServiceTechStack(
            classname=classname, title=title, desc=desc, icon=icon, type=type
        )
        session.add(item)
        session.commit()
    return {"details": "Successfully Saved"}


@route.get("/get-service-tech-stack", response_model=List[ServiceTechStack])
def get_service_tech_stack():
    with get_session() as session:
        stmt = select(ServiceTechStack)
        results = session.exec(stmt).fetchall()
        return results


@route.get("/add-faq")
def add_faq(label: str, content: str):
    with get_session() as session:
        item = FAQ(label=label, content=content)
        session.add(item)
        session.commit()
    return {"details": "Successfully Saved"}


@route.get("/get-faq", response_model=List[FAQ])
def get_faq():
    with get_session() as session:
        stmt = select(FAQ)
        results = session.exec(stmt).fetchall()
        return results

@route.post("/send-email-message")
async def send_email_message(subject: str, content: str, mail_from: str) -> dict:
    #
    message = EmailMessage()
    message["From"] = mail_from
    message["To"] = SMTP_USERNAME
    message["Subject"] = subject
    message.set_content(content)
    # 
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_SERVER, int(SMTP_PORT), context=context) as server:
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(message)
        return {"status": "success", "message": "Email envoyé"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
