from sqlmodel import SQLModel, Field
from src.core.config import ENGINE


class ServiceTechStack(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    classname: str
    title: str
    desc: str
    icon: str
    type: str  # 'service' | 'techstack'


class FAQ(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    label: str
    content: str


def create_table():
    SQLModel.metadata.create_all(ENGINE)
