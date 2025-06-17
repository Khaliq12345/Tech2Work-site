from sqlmodel import Session
from contextlib import contextmanager
from src.core.config import ENGINE


@contextmanager
def get_session():
    session = Session(ENGINE)
    try:
        yield session
    except Exception as e:
        print(f"DB error - {e}")
    finally:
        session.close()
