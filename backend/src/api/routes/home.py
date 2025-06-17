from typing import List
from fastapi import APIRouter
from sqlmodel import select
from src.models.home_models import HomeService, create_table
from src.utils import get_session

route = APIRouter(prefix="/home")
route.add_event_handler("startup", create_table)


@route.get("/add-service")
def add_home_service():
    with get_session() as session:
        service_1 = HomeService(
            classname="classname",
            title="Title",
            description="Description",
            icon="Icon",
            features=["Feature1", "Feature2"],
        )
        session.add(service_1)
        session.commit()
    return {"details": "Working fine"}


@route.get("/get-home-services", response_model=List[HomeService])
def get_home_service():
    with get_session() as session:
        stmt = select(HomeService)
        results = session.exec(stmt).fetchall()
        return results
