from unittest import result
from fastapi import APIRouter
from sqlmodel import select
from src.models.industry_models import IndustryDetails, IndustryFeature, IndustryProcess, IndustryReason, IndustryService, IndustrySolution, IndustryTestimonial, create_table
from src.utils import (
    get_session,
)

route = APIRouter(prefix="/industries")
route.add_event_handler("startup", create_table)

@route.get("/add-industry-detail")
def add_industry_detail(
    name: str, desc: str, bgimg: str, title: str
):
    with get_session() as session:
        item = IndustryDetails(
            name=name,
            desc=desc,
            bgimg=bgimg,
            title=title,
        )
        session.add(item)
        session.commit()
    return {"details": "Successfully Saved"}

@route.get("/get-industry-details")
def get_industry_details(industry: str):
    with get_session() as session:
        stmt = select(IndustryDetails).where(IndustryDetails.name == industry)
        results = session.exec(stmt).fetchall()
        return results
    
@route.get("/add-industry-testimonial")
def add_industry_testimonial(
    industry: str, quote: str, name: str, role: str, avatar: str
):
    with get_session() as session:
        item = IndustryTestimonial(
            industry=industry,
            quote=quote,
            name=name,
            role=role,
            avatar=avatar,
        )
        session.add(item)
        session.commit()
    return {"details": "Successfully Saved"}
   
@route.get("/get-industry-testimonials")
def get_industry_testimonial(industry: str):
    with get_session() as session:
        stmt = select(IndustryTestimonial).where(IndustryTestimonial.industry == industry)
        results = session.exec(stmt).fetchall()
        return results
 
@route.get("/add-industry-service")
def add_industry_service(
    classname: str, title: str, desc: str, icon: str, industry: str
):
    with get_session() as session:
        item = IndustryService(
            classname=classname,
            title=title,
            desc=desc,
            icon=icon,
            industry=industry,
        )
        session.add(item)
        session.commit()
    return {"details": "Successfully Saved"}
 
@route.get("/get-industry-services")
def get_industry_service(industry: str):
    with get_session() as session:
        stmt = select(IndustryService).where(IndustryService.industry == industry)
        results = session.exec(stmt).fetchall()
        return results
    
@route.post("/add-industry-solution")
def add_industry_solution(
    classname: str, title: str, description: str, icon: str, features: list[str], industry: str
):
    with get_session() as session:
        item = IndustrySolution(
            classname=classname,
            title=title,
            desc=description,
            icon=icon,
            features=features,
            industry=industry,
        )
        session.add(item)
        session.commit()
    return {"details": "Successfully Saved"}
    
@route.get("/get-industry-solutions")
def get_industry_solution(industry: str):
    with get_session() as session:
        print(industry)
        stmt = select(IndustrySolution).where(IndustrySolution.industry == industry)
        results = session.exec(stmt).fetchall()
        print(result)
        return results
   
@route.get("/add-industry-feature")
def add_industry_feature(industry: str, title: str, icon: str, classname: str):
    with get_session() as session:
        item = IndustryFeature(title=title, icon=icon, classname=classname, industry=industry)
        session.add(item)
        session.commit()
    return {"details": "Successfully Saved"}
   
@route.get("/get-industry-features")
def get_industry_features(industry: str):
    with get_session() as session:
        stmt = select(IndustryFeature).where(IndustryFeature.industry == industry)
        results = session.exec(stmt).fetchall()
        return results

@route.get("/add-industry-reason")
def add_industry_reason(industry: str, title: str, content: str):
    with get_session() as session:
        item = IndustryReason(title=title, content=content, industry=industry)
        session.add(item)
        session.commit()
    return {"details": "Successfully Saved"}
   
@route.get("/get-industry-reasons")
def get_industry_reason(industry: str):
    with get_session() as session:
        stmt = select(IndustryReason).where(IndustryReason.industry == industry)
        results = session.exec(stmt).fetchall()
        return results

@route.get("/add-industry-process")
def add_industry_process(industry: str, name: str, description: str):
    with get_session() as session:
        item = IndustryProcess(name=name, description=description, industry=industry)
        session.add(item)
        session.commit()
    return {"details": "Successfully Saved"}
   
@route.get("/get-industry-process")
def get_industry_process(industry: str):
    with get_session() as session:
        stmt = select(IndustryProcess).where(IndustryProcess.industry == industry)
        results = session.exec(stmt).fetchall()
        return results