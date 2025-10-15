from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from ..database import SessionLocal
from ..models import Payment
from ..schemas import PaymentSchema
from ..utils import log_event
from datetime import datetime

router = APIRouter(prefix="/api/payments", tags=["Payments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.get("/", response_model=List[PaymentSchema])
def get_payments(
    page: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    status: Optional[str] = Query(None),
    date_from: Optional[str] = Query(None),  # ISO date YYYY-MM-DD
    date_to: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    q = db.query(Payment)
    if status:
        q = q.filter(Payment.status == status)
    if date_from:
        q = q.filter(Payment.date >= datetime.fromisoformat(date_from))
    if date_to:
        q = q.filter(Payment.date <= datetime.fromisoformat(date_to))
    items = q.order_by(Payment.date.desc()).offset(page * limit).limit(limit).all()
    
    # convert datetime -> str for Pydantic
    for item in items:
        item.date = item.date.isoformat()

    log_event("payments", f"Fetched payments page={page} limit={limit} status={status} date_from={date_from} date_to={date_to}")
    return items
