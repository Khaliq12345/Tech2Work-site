from fastapi import FastAPI
from src.api.routes import home

app = FastAPI(title="Tech2Work API")


app.include_router(home.route, tags=["HOME"])
