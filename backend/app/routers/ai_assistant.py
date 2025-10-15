from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Dict
from datetime import datetime, timedelta
from ..database import SessionLocal
from .. import models, schemas
from ..utils import log_event

router = APIRouter(prefix="/api/ai-assistant", tags=["AI Assistant"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def ai_assistant(query: schemas.AIQuery, db: Session = Depends(get_db)) -> Dict:
    """
    Mock AI assistant:
    - Uses simple keyword parsing (invoice/payment/last month) to run DB queries
    - Returns a context-aware answer derived from the DB
    - Logs prompt, response, and timestamp in memory (utils.logs)
    - Clearly marked as mock: replace the inner logic with a real LLM call if available
    """
    user_query = query.query.strip()
    lc = user_query.lower()
    timestamp = datetime.utcnow().isoformat()

    try:
        if "invoice" in lc:
            invoices = db.query(models.Invoice).all()
            total = sum(i.total or 0 for i in invoices)
            unpaid = sum(1 for i in invoices if i.status == "unpaid")
            response = f"Found {len(invoices)} invoices; unpaid: {unpaid}; total value: ${total:,.2f}."
        elif "payment" in lc:
            payments = db.query(models.Payment).all()
            total = sum(p.amount or 0 for p in payments)
            paid_count = sum(1 for p in payments if p.status == "paid")
            response = f"Found {len(payments)} payments; paid: {paid_count}; total paid amount: ${total:,.2f}."
        elif "last month" in lc:
            # compute last month range
            today = datetime.utcnow()
            first_of_current = today.replace(day=1)
            last_month_end = first_of_current - timedelta(days=1)
            last_month_start = last_month_end.replace(day=1)
            payments = db.query(models.Payment).filter(models.Payment.date >= last_month_start, models.Payment.date <= last_month_end).all()
            invoices = db.query(models.Invoice).filter(models.Invoice.date >= last_month_start, models.Invoice.date <= last_month_end).all()
            response = f"Last month ({last_month_start.strftime('%Y-%m')}): {len(payments)} payments, {len(invoices)} invoices."
        else:
            # fallback mock; suggest queries the assistant understands
            response = "I can summarize payments or invoices. Try: 'Show invoices from last month' or 'How many payments this month?'"

        # Log prompt and response (in utils.logs via log_event)
        log_event("ai_assistant", f"Query: {user_query} || Response: {response}")
        return {"query": user_query, "response": response, "timestamp": timestamp}
    except Exception as e:
        log_event("ai_assistant", f"Query: {user_query}", str(e))
        return {"query": user_query, "response": f"Error: {str(e)}", "timestamp": timestamp}
