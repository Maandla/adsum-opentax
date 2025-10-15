import React, { useState } from "react";
import { sendAIQuery } from "../hooks/useApi";

export default function AIChatPanel() {
  const [input, setInput] = useState("");
  const [history, setHistory] = useState<{ query: string; response: string; timestamp?: string }[]>([]);
  const [loading, setLoading] = useState(false);

  const onSend = async () => {
    if (!input.trim()) return;
    setLoading(true);
    try {
      const data = await sendAIQuery(input);
      // backend returns { query, response, timestamp }
      setHistory((h) => [...h, { query: data.query, response: data.response, timestamp: data.timestamp }]);
    } catch (e) {
      setHistory((h) => [...h, { query: input, response: "Error getting response" }]);
    } finally {
      setInput("");
      setLoading(false);
    }
  };

  return (
    <div className="bg-white p-4 rounded shadow">
      <h3 className="font-semibold mb-2">AI Assistant</h3>
      <div className="h-48 overflow-auto mb-2 border p-2">
        {history.length === 0 ? <div className="text-gray-500">No conversation yet — ask something like "Show invoices from last month"</div> : null}
        {history.map((m, i) => (
          <div key={i} className="mb-2">
            <div className="text-blue-600 text-sm">You: {m.query}</div>
            <div className="text-gray-800 text-sm">Bot: {m.response}</div>
            {m.timestamp ? <div className="text-xs text-gray-400">{m.timestamp}</div> : null}
          </div>
        ))}
      </div>

      <div className="flex gap-2">
        <input className="flex-1 border p-2 rounded" value={input} onChange={(e) => setInput(e.target.value)} placeholder='e.g. "Show invoices from last month"' onKeyDown={(e) => e.key === "Enter" && onSend()} />
        <button className="px-3 py-2 bg-blue-600 text-white rounded" onClick={onSend} disabled={loading}>{loading ? "..." : "Send"}</button>
      </div>
    </div>
  );
}
