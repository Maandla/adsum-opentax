from fastapi import APIRouter
from ..utils import logs

router = APIRouter(prefix="/api/agent-logs", tags=["Agent Logs"])

@router.get("/")
def get_agent_logs(limit: int = 50):
    # return most recent 'limit' entries (default 50)
    return logs[-limit:]
