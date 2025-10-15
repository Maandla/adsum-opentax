from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, SessionLocal, Base
from .models import Payment, Invoice
from .routers import payments, invoices, summary, ai_assistant, logs as agent_logs
from datetime import datetime, timedelta
import random
from faker import Faker

app = FastAPI(title="OpenTax Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create tables
Base.metadata.create_all(bind=engine)

# seed DB with 25 payments + 25 invoices if empty
fake = Faker()
db = SessionLocal()
if db.query(Payment).count() == 0:
    for _ in range(25):
        db.add(Payment(
            amount=round(random.uniform(50, 2000), 2),
            status=random.choice(["paid", "unpaid"]),
            date=fake.date_time_between(start_date='-90d', end_date='now')
        ))
if db.query(Invoice).count() == 0:
    for _ in range(25):
        db.add(Invoice(
            total=round(random.uniform(100, 5000), 2),
            status=random.choice(["paid", "unpaid"]),
            date=fake.date_time_between(start_date='-90d', end_date='now')
        ))
db.commit()
db.close()

# include routers
app.include_router(payments.router)
app.include_router(invoices.router)
app.include_router(summary.router)
app.include_router(ai_assistant.router)
app.include_router(agent_logs.router)

@app.get("/")
def root():
    return {"message": "OpenTax Backend running"}
