from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from collections import defaultdict
from ..database import SessionLocal
from ..models import Payment, Invoice
from ..utils import log_event

router = APIRouter(prefix="/api/summary", tags=["Summary"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_summary(db: Session = Depends(get_db)):
    payments = db.query(Payment).all()
    invoices = db.query(Invoice).all()

    # totals
    total_payments_amount = sum((p.amount or 0) for p in payments)
    unpaid_invoices = sum(1 for i in invoices if i.status == "unpaid")

    # monthly totals (YYYY-MM)
    monthly_payments = defaultdict(float)
    monthly_invoices = defaultdict(float)
    for p in payments:
        k = p.date.strftime("%Y-%m")
        monthly_payments[k] += p.amount or 0
    for i in invoices:
        k = i.date.strftime("%Y-%m")
        monthly_invoices[k] += i.total or 0

    payload = {
        "total_payments": total_payments_amount,
        "unpaid_invoices": unpaid_invoices,
        "monthly_payments": dict(monthly_payments),
        "monthly_invoices": dict(monthly_invoices),
    }
    log_event("summary", "Computed summary")
    return payload
