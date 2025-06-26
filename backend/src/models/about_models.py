from sqlmodel import SQLModel, Field
from src.core.config import ENGINE

class AboutValue(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    icon: str
    desc: str

def create_table():
    SQLModel.metadata.create_all(ENGINE)
