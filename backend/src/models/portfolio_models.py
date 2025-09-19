from sqlmodel import JSON, SQLModel, Field
from src.core.config import ENGINE

class PortfolioProject(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    location: str
    technologies: list[str] = Field(sa_type=JSON)
    services: list[str] = Field(sa_type=JSON)
    industries: list[str] = Field(sa_type=JSON)
    imgUrl: str
    locale: str

def create_table():
    SQLModel.metadata.create_all(ENGINE)
