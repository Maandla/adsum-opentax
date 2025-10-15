from datetime import datetime
from typing import List, Dict

# in-memory logs list
logs: List[Dict] = []

def log_event(event_type: str, message: str, error: str | None = None):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,   # e.g. "payments", "invoices", "summary", "ai_assistant"
        "message": message,
        "error": error,
    }
    logs.append(entry)
    # cap log length to avoid unbounded growth
    if len(logs) > 1000:
        del logs[0:200]
