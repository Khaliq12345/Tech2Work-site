from fastapi import FastAPI
from src.api.routes import home, industries, globals
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Tech2Work API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prefix="/api", router=home.route, tags=["HOME"])
app.include_router(prefix="/api", router=globals.route, tags=["GLOBAL"])
app.include_router(prefix="/api", router=industries.route, tags=["INDUSTRIES"])
