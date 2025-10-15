from pydantic import BaseModel

class PaymentSchema(BaseModel):
    id: int
    amount: float
    status: str
    date: str

    model_config = {"from_attributes": True}

class InvoiceSchema(BaseModel):
    id: int
    total: float
    status: str
    date: str

    model_config = {"from_attributes": True}

class AIQuery(BaseModel):
    query: str
