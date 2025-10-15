import React from "react";

interface Props {
  totalPayments: number;
  unpaidInvoices: number;
}

const DashboardMetrics: React.FC<Props> = ({ totalPayments, unpaidInvoices }) => {
  return (
    <div className="grid grid-cols-2 gap-4 mb-6">
      <div className="p-4 bg-white shadow rounded">
        <h2 className="text-gray-500">Total Payments</h2>
        <p className="text-2xl font-bold">{totalPayments}</p>
      </div>
      <div className="p-4 bg-white shadow rounded">
        <h2 className="text-gray-500">Unpaid Invoices</h2>
        <p className="text-2xl font-bold">{unpaidInvoices}</p>
      </div>
    </div>
  );
};

export default DashboardMetrics;
