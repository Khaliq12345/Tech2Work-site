# from typing import List
from fastapi import APIRouter

# from sqlmodel import select
from src.models.home_models import (
    create_table,
)  # , HomeService, HomeTestimonial, ServiceTechStack, HomeIndustry, HomeProcess, FAQ
# from src.utils import get_session

route = APIRouter(prefix="/industries")
route.add_event_handler("startup", create_table)
