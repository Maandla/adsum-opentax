import AIChatPanel from "../components/AIPanel";
import { useSummary, usePayments, useInvoices, useLogs } from "../hooks/useApi";
import DashboardMetrics from "../components/DashboardMetrics";
import Chart from "../components/Chart";
import PaymentsTable from "../components/PaymentsTable";
import { useState } from "react";

export default function Home() {
  const { data: summary } = useSummary();
  const [paymentsPage, setPaymentsPage] = useState(0);
  const [invoicesPage, setInvoicesPage] = useState(0);
  const [paymentsStatus, setPaymentsStatus] = useState("");
  const [invoicesStatus, setInvoicesStatus] = useState("");

  const { data: payments } = usePayments(paymentsPage, 10, paymentsStatus);
  const { data: invoices } = useInvoices(invoicesPage, 10, invoicesStatus);
  const { data: logs } = useLogs();

  return (
    <div className="p-6 space-y-6">

      {}
      {summary && (
        <DashboardMetrics
          totalPayments={summary.total_payments}
          unpaidInvoices={summary.unpaid_invoices}
        />
      )}

      {}
      {summary && (
        <Chart
          data={Object.keys(summary.monthly_payments).reduce((acc, key) => {
            acc[key] = {
              payments: summary.monthly_payments[key] || 0,
              invoices: summary.monthly_invoices[key] || 0,
            };
            return acc;
          }, {} as Record<string, { payments: number; invoices: number }>)}
        />
      )}

      {}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

        {}
        <div className="bg-white shadow rounded p-4">
          <div className="flex justify-between mb-2">
            <h2 className="font-bold">Payments</h2>
            <select
              className="border p-1 rounded"
              value={paymentsStatus}
              onChange={(e) => setPaymentsStatus(e.target.value)}
            >
              <option value="">All</option>
              <option value="paid">Paid</option>
              <option value="unpaid">Unpaid</option>
            </select>
          </div>
          {payments && <PaymentsTable payments={payments} />}
          <div className="flex justify-between mt-2">
            <button
              className="px-2 py-1 border rounded"
              disabled={paymentsPage === 0}
              onClick={() => setPaymentsPage((p) => p - 1)}
            >
              Prev
            </button>
            <button
              className="px-2 py-1 border rounded"
              disabled={!payments || payments.length < 10}
              onClick={() => setPaymentsPage((p) => p + 1)}
            >
              Next
            </button>
          </div>
        </div>

        {/* Invoices Table */}
        <div className="bg-white shadow rounded p-4">
          <div className="flex justify-between mb-2">
            <h2 className="font-bold">Invoices</h2>
            <select
              className="border p-1 rounded"
              value={invoicesStatus}
              onChange={(e) => setInvoicesStatus(e.target.value)}
            >
              <option value="">All</option>
              <option value="paid">Paid</option>
              <option value="unpaid">Unpaid</option>
            </select>
          </div>
          {invoices && (
            <div className="overflow-auto max-h-64">
              <table className="w-full border">
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>Total</th>
                    <th>Date</th>
                    <th>Status</th>
                  </tr>
                </thead>
                <tbody>
                  {invoices.map((i: any) => (
                    <tr key={i.id}>
                      <td>{i.id}</td>
                      <td>{i.total}</td>
                      <td>{new Date(i.date).toLocaleDateString()}</td>
                      <td>{i.status}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
          <div className="flex justify-between mt-2">
            <button
              className="px-2 py-1 border rounded"
              disabled={invoicesPage === 0}
              onClick={() => setInvoicesPage((p) => p - 1)}
            >
              Prev
            </button>
            <button
              className="px-2 py-1 border rounded"
              disabled={!invoices || invoices.length < 10}
              onClick={() => setInvoicesPage((p) => p + 1)}
            >
              Next
            </button>
          </div>
        </div>
      </div>

      {/* 4. AI Chat and Logs */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <AIChatPanel />
        <div className="bg-white p-4 rounded shadow">
          <h3 className="font-semibold mb-2">Recent Logs</h3>
          <div className="h-48 overflow-auto text-sm">
            {logs?.length ? logs.map((l: any, idx: number) => (
              <div key={idx} className="mb-2">
                <div><strong>{l.event_type}</strong> — {l.message}</div>
                <div className="text-xs text-gray-400">{l.timestamp}{l.error ? ` — error: ${l.error}` : ""}</div>
              </div>
            )) : <div className="text-gray-500">No logs yet.</div>}
          </div>
        </div>
      </div>

    </div>
  );
}