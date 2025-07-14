from sqlmodel import create_engine
import os
from dotenv import load_dotenv

load_dotenv(".env")

ENGINE = create_engine("sqlite:///database.db")
APP_MAIL_ADRESS = os.getenv('APP_MAIL_ADRESS') or ''
APP_MAIL_PASSWORD = os.getenv('APP_MAIL_PASSWORD') or ''
TO_MAIL_ADRESS = os.getenv('TO_MAIL_ADRESS') or ''