from sqlmodel import JSON, SQLModel, Field

from src.core.config import ENGINE


class HomeService(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    classname: str
    title: str
    description: str
    icon: str
    features: list[str] = Field(sa_type=JSON)


def create_table():
    SQLModel.metadata.create_all(ENGINE)
