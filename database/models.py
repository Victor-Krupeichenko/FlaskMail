from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class Recipient(Base):
    """Модель информации о получателе"""
    __tablename__ = "recipient"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    name = Column(String(50))
    status = Column(String, default="awaiting mailing")
    date = Column(DateTime, default=datetime.utcnow)
    count_sent = Column(Integer, default=0)

    def __repr__(self):
        return f"name: {self.name} -> email: {self.email}"
