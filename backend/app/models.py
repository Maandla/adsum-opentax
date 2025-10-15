from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from .database import Base

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    status = Column(String, nullable=False, default="paid")  # paid/unpaid
    date = Column(DateTime, default=datetime.utcnow)

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True, index=True)
    total = Column(Float, nullable=False)
    status = Column(String, nullable=False, default="unpaid")  # paid/unpaid
    date = Column(DateTime, default=datetime.utcnow)
