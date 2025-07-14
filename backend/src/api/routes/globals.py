from typing import List
from fastapi import APIRouter
from sqlmodel import select
from src.models.global_models import create_table, ServiceTechStack, FAQ
from src.utils import get_session

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

