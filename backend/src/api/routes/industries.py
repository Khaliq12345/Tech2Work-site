# from typing import List
from fastapi import APIRouter
from sqlmodel import select

# from sqlmodel import select
from src.models.home_models import (
    HomeService,
    create_table,
)
from utils import (
    get_session,
)  # , HomeService, HomeTestimonial, ServiceTechStack, HomeIndustry, HomeProcess, FAQ
# from src.utils import get_session

route = APIRouter(prefix="/industries")
route.add_event_handler("startup", create_table)


@route.get("/get-industry-services")
def get_industry_service(industry: str):
    with get_session() as session:
        stmt = select(HomeService).where(HomeService.description == industry)
        session.exec(stmt)
