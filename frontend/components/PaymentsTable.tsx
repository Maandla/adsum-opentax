export default function PaymentsTable({ payments }: { payments: any[] }) {
  return (
    <div className="bg-white shadow rounded p-4">
      <h2 className="font-bold mb-2">Payments</h2>
      <table className="w-full border">
        <thead>
          <tr>
            <th>ID</th><th>Amount</th><th>Date</th><th>Status</th>
          </tr>
        </thead>
        <tbody>
          {payments.map(p => (
            <tr key={p.id}>
              <td>{p.id}</td>
              <td>{p.amount}</td>
              <td>{new Date(p.date).toLocaleDateString()}</td>
              <td>{p.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
