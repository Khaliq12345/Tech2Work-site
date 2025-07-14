from sqlmodel import create_engine
import os
from dotenv import load_dotenv

load_dotenv(".env")

ENGINE = create_engine("sqlite:///database.db")
SMTP_USERNAME = os.getenv('SMTP_USERNAME') or ''
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD') or ''
SMTP_SERVER = os.getenv('SMTP_SERVER') or ''
SMTP_PORT = os.getenv('SMTP_PORT') or ''