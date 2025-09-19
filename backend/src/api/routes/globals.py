from typing import List
from fastapi import APIRouter, BackgroundTasks
from sqlmodel import select
from src.models.global_models import (
    create_table,
    ServiceTechStack,
    FAQ,
    TermsOfUseLiability,
    PrivacyDetailPart,
    PrivacyDetailItem,
)
from src.utils import get_session, send_email_message


route = APIRouter(prefix="/global")
route.add_event_handler("startup", create_table)


@route.get("/add-service-tech-stack")
def add_service_tech_stack(classname: str, title: str, desc: str, icon: str, type: str):
    with get_session() as session:
        item = ServiceTechStack(
            classname=classname,
            title=title,
            desc=desc,
            icon=icon,
            type=type,
            locale="en",
        )
        session.add(item)
        session.commit()
    return {"details": "Successfully Saved"}


@route.get("/get-service-tech-stack", response_model=List[ServiceTechStack])
def get_service_tech_stack(locale: str):
    with get_session() as session:
        stmt = select(ServiceTechStack).where(ServiceTechStack.locale == locale)
        results = session.exec(stmt).fetchall()
        return results


@route.get("/add-faq")
def add_faq(label: str, content: str):
    with get_session() as session:
        item = FAQ(label=label, content=content, locale="en")
        session.add(item)
        session.commit()
    return {"details": "Successfully Saved"}


@route.get("/get-faq", response_model=List[FAQ])
def get_faq(locale: str):
    with get_session() as session:
        stmt = select(FAQ).where(FAQ.locale == locale)
        results = session.exec(stmt).fetchall()
        return results


@route.post("/send-email-message")
def send_email(background_tasks: BackgroundTasks, subject: str, content: str):
    background_tasks.add_task(send_email_message, subject, content)
    return {"status": "success", "message": "Envoi en cours…"}


@route.get("/add-terms-of-use-liability")
def add_terms_of_use_liability(value: str):
    with get_session() as session:
        item = TermsOfUseLiability(value=value, locale="en")
        session.add(item)
        session.commit()
    return {"details": "Successfully Saved"}


@route.get("/get-terms-of-use-liability", response_model=List[TermsOfUseLiability])
def get_terms_of_use_liability(locale: str):
    with get_session() as session:
        stmt = select(TermsOfUseLiability).where(TermsOfUseLiability.locale == locale)
        results = session.exec(stmt).fetchall()
        return results


@route.post("/add-privacy-detail-item-test")
def add_privacy_detail_item_test():
    with get_session() as session:
        part1 = PrivacyDetailPart(
            subtitle="Personal information you disclose to us",
            summary="We collect personal information that you provide to us.",
            details=["Full name", "Phone number"],
            locale="en",
        )

        part2 = PrivacyDetailPart(
            subtitle="Sensitive Information",
            summary="We do not intentionally collect or process sensitive personal data unless required by law.",
            details=[],
            locale="en",
        )

        item = PrivacyDetailItem(
            title="1. What information do we collect?",
            parts=[part1.model_dump(), part2.model_dump()],
            locale="en",
        )

        print(item)

        session.add(item)
        session.commit()
    return {"details": "Successfully Saved"}


@route.get("/get-privacy-detail", response_model=List[PrivacyDetailItem])
def get_privacy_detail(locale: str):
    with get_session() as session:
        stmt = select(PrivacyDetailItem).where(PrivacyDetailItem.locale == locale)
        results = session.exec(stmt).fetchall()
        return results
