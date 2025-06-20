from typing import List
from fastapi import APIRouter
from sqlmodel import select
from src.models.portfolio_models import create_table, PortfolioProject
from src.utils import get_session

route = APIRouter(prefix="/portfolio")
route.add_event_handler("startup", create_table)


@route.post("/add-portfolio-project")
def add_portfolio_project(
    title: str,
    description: str,
    location: str,
    technologies: list[str],
    services: list[str],
    industries: list[str],
    imgUrl: str,
):
    with get_session() as session:
        item = PortfolioProject(
            title=title,
            description=description,
            location=location,
            technologies=technologies,
            services=services,
            industries=industries,
            imgUrl=imgUrl,
        )
        session.add(item)
        session.commit()
    return {"details": "Successfully Saved"}


@route.get("/get-portfolio-projects", response_model=List[PortfolioProject])
def get_portfolio_projects():
    with get_session() as session:
        stmt = select(PortfolioProject)
        results = session.exec(stmt).fetchall()
        return results
