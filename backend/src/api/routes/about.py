from fastapi import APIRouter
from sqlmodel import select
from src.models.about_models import AboutValue, create_table
from src.utils import (
    get_session,
)

route = APIRouter(prefix="/about")
route.add_event_handler("startup", create_table)


@route.get("/add-about-value")
def add_about_value(title: str, desc: str, icon: str):
    with get_session() as session:
        item = AboutValue(title=title, desc=desc, icon=icon, locale="en")
        session.add(item)
        session.commit()
    return {"details": "Successfully Saved"}


@route.get("/get-about-value")
def get_about_value(locale: str):
    with get_session() as session:
        stmt = select(AboutValue).where(AboutValue.locale == locale)
        results = session.exec(stmt).fetchall()
        return results
