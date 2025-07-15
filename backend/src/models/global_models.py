from typing import Any, Dict
from sqlmodel import SQLModel, JSON, Field
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
    
    
class TermsOfUseLiability(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    value: str
    
    
class PrivacyDetailPart(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    subtitle: str
    summary: str
    details: list[str] = Field(sa_type=JSON)


class PrivacyDetailItem(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    parts: list[Dict[str, Any] ] = Field(sa_type=JSON)

def create_table():
    SQLModel.metadata.create_all(ENGINE)
