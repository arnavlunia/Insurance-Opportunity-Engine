import { useEffect, useState } from "react";
import { getOpportunities } from "./api/client";

type Client = {
  client_id: number;
  name: string;
  score: number;
  segment: string;
  reasons: string[];
  next_best_action: {
    action: string;
    product: string;
    message: string;
  };
};

export default function App() {
  const [clients, setClients] = useState<Client[]>([]);

  useEffect(() => {
    getOpportunities()
      .then((data) => {
        console.log("RAW API:", data);   
  
        setClients(data.opportunities || data || []);
      })
      .catch(console.error);
  }, []);

  return (
    <div style={{ padding: 20, fontFamily: "Arial" }}>
      <h1>Insurance Opportunity Engine</h1>

      <div style={{ display: "grid", gap: 12 }}>
        {clients.map((c) => (
          <div key={c.client_id} style={{ border: "1px solid #ccc", padding: 12 }}>
            <h3>{c.name}</h3>
            <p>Score: {c.score}</p>
            <p>Segment: {c.segment}</p>

            <strong>Reasons:</strong>
            <ul>
              {(c.reasons || []).map((r, i) => (
                <li key={i}>{r}</li>
              ))}
            </ul>

            <p><b>Next Action:</b> {c.next_best_action?.action}</p>
            <p>{c.next_best_action?.message}</p>
          </div>
        ))}
      </div>
    </div>
  );
}