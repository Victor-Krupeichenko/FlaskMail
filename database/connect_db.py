from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.url_database import _URL

engine = create_engine(url=_URL)
session_maker = sessionmaker(engine, expire_on_commit=False)
