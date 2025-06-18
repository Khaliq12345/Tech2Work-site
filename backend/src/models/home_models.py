from sqlmodel import JSON, SQLModel, Field
from src.core.config import ENGINE


class HomeService(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    classname: str
    title: str
    description: str
    icon: str
    features: list[str] = Field(sa_type=JSON)


class HomeTestimonial(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    classname: str
    quote: str
    name: str
    role: str
    avatar: str


class HomeIndustry(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    icon: str
    description: str
    samples: list[str] = Field(sa_type=JSON)


class HomeProcess(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str


def create_table():
    SQLModel.metadata.create_all(ENGINE)
