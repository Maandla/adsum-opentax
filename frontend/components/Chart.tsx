import { Bar } from 'react-chartjs-2'
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement } from 'chart.js'

ChartJS.register(CategoryScale, LinearScale, BarElement)

export default function Chart({ data }: { data: any }) {
  const labels = Object.keys(data)
  const payments = labels.map(l => data[l].payments)
  const invoices = labels.map(l => data[l].invoices)

  return (
    <div className="bg-white p-4 shadow rounded mb-6">
      <Bar
        data={{
          labels,
          datasets: [
            { label: 'Payments', data: payments, backgroundColor: 'rgba(34,197,94,0.7)' },
            { label: 'Invoices', data: invoices, backgroundColor: 'rgba(59,130,246,0.7)' }
          ]
        }}
      />
    </div>
  )
}
