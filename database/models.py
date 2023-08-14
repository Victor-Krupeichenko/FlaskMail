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

    def __repr__(self):
        return f"name: {self.name} -> email: {self.email}"


class MailHistory(Base):
    """Модель истории рассылок"""
    __tablename__ = "mail_history"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    sent = Column(Integer)
    delivered = Column(Integer)
    not_delivered = Column(Integer)

    def __repr__(self):
        return f"date: {self.date} -> sent: {self.sent}"
