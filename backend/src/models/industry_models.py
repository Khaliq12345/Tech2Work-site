from sqlmodel import JSON, SQLModel, Field
from src.core.config import ENGINE

class IndustryDetails(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    bgimg: str
    desc: str
    title: str


class IndustryService(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    classname: str
    title: str
    desc: str
    icon: str
    industry: str


class IndustryTestimonial(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    quote: str
    name: str
    role: str
    avatar: str
    industry: str


class IndustrySolution(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    classname: str
    title: str
    desc: str
    icon: str
    features: list[str] = Field(sa_type=JSON)
    industry: str
    
class IndustryFeature(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    classname: str
    title: str
    icon: str
    industry: str


class IndustryReason(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str
    industry: str


class IndustryProcess(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str
    industry: str


def create_table():
    SQLModel.metadata.create_all(ENGINE)
