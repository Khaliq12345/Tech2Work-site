from typing import List
from fastapi import APIRouter
from sqlmodel import select
from src.models.home_models import (
    create_table,
    HomeService,
    HomeTestimonial,
    HomeIndustry,
    HomeProcess,
)
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
            features=features,
        )
        session.add(item)
        session.commit()
    return {"details": "Successfully Saved"}



@route.get("/get-home-services", response_model=List[HomeService])
def get_home_services():
    with get_session() as session:
        stmt = select(HomeService)
        results = session.exec(stmt).fetchall()
        return results




@route.get("/add-home-testimonial")
def add_home_testimonial(
    classname: str, quote: str, name: str, role: str, avatar: str
):
def add_home_testimonial(
    classname: str, quote: str, name: str, role: str, avatar: str
):
    with get_session() as session:
        item = HomeTestimonial(
            classname=classname,
            quote=quote,
            name=name,
            role=role,
            avatar=avatar,
            avatar=avatar,
        )
        session.add(item)
        session.commit()
    return {"details": "Successfully Saved"}

@route.get("/get-home-testimonials", response_model=List[HomeTestimonial])
def get_home_testimonials():
    with get_session() as session:
        stmt = select(HomeTestimonial)
        results = session.exec(stmt).fetchall()
        return results




@route.post("/add-home-industry")
def add_home_industry(
    name: str, description: str, icon: str, samples: list[str]
): 
    with get_session() as session:
        item = HomeIndustry(
            name=name, description=description, icon=icon, samples=samples
            name=name, description=description, icon=icon, samples=samples
        )
        session.add(item)
        session.commit()
    return {"details": "Successfully Saved"}




@route.get("/get-home-industries", response_model=List[HomeIndustry])
def get_home_industries():
    with get_session() as session:
        stmt = select(HomeIndustry)
        results = session.exec(stmt).fetchall()
        return results




@route.get("/add-home-process")
def add_home_process(title: str, content: str):
    with get_session() as session:
        item = HomeProcess(title=title, content=content)
        item = HomeProcess(title=title, content=content)
        session.add(item)
        session.commit()
    return {"details": "Successfully Saved"}




@route.get("/get-home-process", response_model=List[HomeProcess])
def get_home_process():
    with get_session() as session:
        stmt = select(HomeProcess)
        results = session.exec(stmt).fetchall()
        return results



