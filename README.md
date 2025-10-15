# OpenTax Full Stack Developer Take-Home Assignment

This project is a simplified Accountant Data Aggregation and Insights Dashboard with AI assistant capabilities.



opentax-startingapp/
├─ backend/
│  ├─ app/
│  │  ├─ main.py
│  │  ├─ models.py
│  │  ├─ database.py
│  │  ├─ schemas.py
│  │  ├─ utils.py
│  │  ├─ routers/
│  │  │  ├─ payments.py
│  │  │  ├─ invoices.py
│  │  │  ├─ summary.py
│  │  │  ├─ ai_assistant.py
│  │  │  └─ logs.py
│  └─ requirements.txt
├─ frontend/
│  ├─ pages/
│  │  ├─ _app.tsx
│  │  └─ index.tsx
│  ├─ components/
│  │  ├─ AIPanel.tsx
│  │  ├─ Charts.tsx
│  │  ├─ DashboardMetrics.tsx
│  │  ├─ PaymentsTable.tsx
│  │  └─ InvoicesTable.tsx
│  ├─ hooks/
│  │  └─ useApi.ts
│  ├─ styles/
│  │  └─ globals.css
│  └─ package.json
├─ README.md
└─ SOLUTION.md


## **Setup Instructions**

### Backend

1. Navigate to backend folder:

cd backend

2.Create a virtual environment:
    python -m venv venv
    source venv/bin/activate  # Linux / macOS
    venv\Scripts\activate  

3.Install dependencies:
    pip install -r requirements.txt

4.Run the backend server:
    uvicorn app.main:app --reload

5.Backend runs at:
    http://localhost:8000



### Frontend Setup
1.Navigate to frontend folder:
   cd frontend

2.Install dependencies:
   npm install

3.Run the development server:
  npm run dev

4.Frontend runs at:
  [npm run dev]
  (http://localhost:3000)
   
Mock Data

Payments: 25 entries, random amount between 50–2000, random status paid/unpaid, random date within last 90 days.

Invoices: 25 entries, random total between 100–5000, random status paid/unpaid, random date within last 90 days.

Data is seeded at backend startup using Faker and stored in SQLite (opentax.db).

Author
Maanda Mufamadi