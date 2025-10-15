from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from ..database import SessionLocal
from ..models import Invoice
from ..schemas import InvoiceSchema
from ..utils import log_event
from datetime import datetime

router = APIRouter(prefix="/api/invoices", tags=["Invoices"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.get("/", response_model=List[InvoiceSchema])
def get_invoices(
    page: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    status: Optional[str] = Query(None),
    date_from: Optional[str] = Query(None),
    date_to: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    q = db.query(Invoice)
    if status:
        q = q.filter(Invoice.status == status)
    if date_from:
        q = q.filter(Invoice.date >= datetime.fromisoformat(date_from))
    if date_to:
        q = q.filter(Invoice.date <= datetime.fromisoformat(date_to))
    items = q.order_by(Invoice.date.desc()).offset(page * limit).limit(limit).all()
    
    # convert datetime -> str
    for item in items:
        item.date = item.date.isoformat()

    log_event("invoices", f"Fetched invoices page={page} limit={limit} status={status} date_from={date_from} date_to={date_to}")
    return items
