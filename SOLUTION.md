# OpenTax Full Stack Developer Assignment — Solution

## Architecture

- Backend: FastAPI + SQLAlchemy + SQLite
  - REST APIs: Payments, Invoices, Summary, AI Assistant, Logs
  - SQLite DB stores mock data for the session
  - Logs all actions in memory
- Frontend: Next.js + React + TypeScript + Tailwind CSS
  - Dashboard page with metrics, charts, tables, AI chat, and logs
  - React Query used for fetching and caching data
- Data Flow: Frontend → React Query → Backend → DB

## Backend

- `/api/payments` → Returns payments (paginated, filterable)
- `/api/invoices` → Returns invoices (paginated, filterable)
- `/api/summary` → Returns total payments, unpaid invoices, monthly breakdowns
- `/api/ai-assistant` → Mock AI assistant that responds to simple queries
- `/api/logs` → Returns recent API activity

- DB Models: Payment, Invoice
- Schemas: Pydantic for validation and serialization
- Utils: `log_event` stores all logs in memory

- Mock data:
  - 25 payments (random amount, status, date)
  - 25 invoices (random total, status, date)
  - Seeded at startup using Faker

## Frontend

- Components:
  - AIPanel → Chat interface for AI Assistant
  - DashboardMetrics → Shows total payments & unpaid invoices
  - Chart → Bar chart of monthly totals
  - PaymentsTable / InvoicesTable → Paginated tables
  - Logs panel → Shows recent logs

- React Query used for state management and caching
- Tailwind CSS for layout and styling
- Responsive design with grid layout

## AI Assistant

- Endpoint: `/api/ai-assistant`
- Mock logic:
  - If query mentions “invoice” → summarize invoices
  - If query mentions “payment” → summarize payments
  - If query mentions “last month” → filter by last month
  - Otherwise → give suggestions for supported queries
- Logs all queries with timestamp

## Observability

- All API calls and AI queries are logged in memory
- Log fields: event_type, message, timestamp, optional error
- Frontend shows last 50 logs in scrollable panel

## Trade-offs and Assumptions

- SQLite used for simplicity and in-memory persistence
- AI Assistant is mocked, not real LLM API
- Pagination is offset-based (simple for small dataset)
- No authentication required
- Focused on functionality, simple styling

## Future Improvements

- Replace AI mock with real LLM API
- Add server-side filtering, sorting, advanced pagination
- Deploy backend + frontend with Docker
- Switch to PostgreSQL for production
- Add authentication
- Add automated tests


