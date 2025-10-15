import { useQuery } from '@tanstack/react-query'
import axios from 'axios'

const API = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api'
export const useSummary = () =>
  useQuery({
    queryKey: ['summary'],
    queryFn: async () => (await axios.get(`${API}/summary`)).data,
  })

export const usePayments = (page = 0, limit = 10, status = '') =>
  useQuery({
    queryKey: ['payments', page, limit, status],
    queryFn: async () =>
      (await axios.get(`${API}/payments`, { params: { page, limit, status } })).data,
  })

export const useInvoices = (page = 0, limit = 10, status = '') =>
  useQuery({
    queryKey: ['invoices', page, limit, status],
    queryFn: async () =>
      (await axios.get(`${API}/invoices`, { params: { page, limit, status } })).data,
  })

export const useLogs = () =>
  useQuery({
    queryKey: ['logs'],
    queryFn: async () => (await axios.get(`${API}/agent-logs`)).data,
  })

export const sendAIQuery = async (q: string) => {
  const res = await axios.post(`${API}/ai-assistant`, { query: q })
  return res.data
}
