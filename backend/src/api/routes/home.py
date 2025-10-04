from typing import List
from fastapi import APIRouter
from sqlmodel import select  # , text
from src.models.home_models import (
    create_table,
    HomeService,
    HomeTestimonial,
    HomeIndustry,
    HomeProcess,
)
from src.utils import get_session

route = APIRouter(prefix="/home")
route.add_event_handler("startup", create_table)


@route.post("/add-home-service")
def add_home_service(
    classname: str, title: str, description: str, icon: str, features: list[str]
):
    with get_session() as session:
        item = HomeService(
            classname=classname,
            title=title,
            description=description,
            icon=icon,
            features=features,
            locale="en",
        )
        session.add(item)
        session.commit()
    return {"details": "Successfully Saved"}


@route.get("/get-home-services", response_model=List[HomeService])
def get_home_services(locale: str):
    with get_session() as session:
        stmt = select(HomeService).where(HomeService.locale == locale)
        results = session.exec(stmt).fetchall()
        return results


@route.get("/add-home-testimonial")
def add_home_testimonial(classname: str, quote: str, name: str, role: str, avatar: str):
    with get_session() as session:
        item = HomeTestimonial(
            classname=classname,
            quote=quote,
            name=name,
            role=role,
            avatar=avatar,
            locale="en",
        )
        session.add(item)
        session.commit()
    return {"details": "Successfully Saved"}


@route.get("/get-home-testimonials", response_model=List[HomeTestimonial])
def get_home_testimonials(locale: str):
    with get_session() as session:
        stmt = select(HomeTestimonial).where(HomeTestimonial.locale == locale)
        results = session.exec(stmt).fetchall()
        return results


@route.post("/add-home-industry")
def add_home_industry(name: str, description: str, icon: str, samples: list[str]):
    with get_session() as session:
        item = HomeIndustry(
            name=name, description=description, icon=icon, samples=samples, locale="en"
        )
        session.add(item)
        session.commit()
    return {"details": "Successfully Saved"}


@route.get("/get-home-industries", response_model=List[HomeIndustry])
def get_home_industries(locale: str):
    with get_session() as session:
        stmt = select(HomeIndustry).where(HomeIndustry.locale == locale)
        results = session.exec(stmt).fetchall()
        return results


@route.get("/add-home-process")
def add_home_process(title: str, content: str):
    with get_session() as session:
        item = HomeProcess(title=title, content=content, locale="en")
        session.add(item)
        session.commit()
    return {"details": "Successfully Saved"}


@route.get("/get-home-process", response_model=List[HomeProcess])
def get_home_process(locale: str):
    with get_session() as session:
        stmt = select(HomeProcess).where(HomeProcess.locale == locale)
        results = session.exec(stmt).fetchall()
        return results


# @route.post("/add-locale-col")
# def add_locale_column():
#     with get_session() as session:
#         for tablee in ['aboutvalue', 'faq', 'homeindustry', 'homeprocess', 'homeservice', 'hometestimonial', 'portfolioproject', 'privacydetailitem', 'servicetechstack', 'termsofuseliability ']:
#             session.exec(
#                 text(f"""
#                     ALTER TABLE {tablee}
#                     ADD COLUMN locale VARCHAR(10) DEFAULT 'en'
#                 """)
#             )
#         session.commit()
