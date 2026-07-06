import { useEffect, useState } from "react";
import { getOpportunities } from "./api/client";
import ClientCard from "./components/ClientCard";
import StatsBar from "./components/StatsBar";

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

  const hot = clients.filter((c) => c.segment === "HOT").length;
  const warm = clients.filter((c) => c.segment === "WARM").length;
  const cold = clients.filter((c) => c.segment === "COLD").length;

  return (
    <div
      style={{
        background: "#f4f6f9",
        minHeight: "100vh",
        padding: "40px",
        fontFamily: "Arial"
      }}
    >
      <h1 style={{ marginBottom: "30px" }}>
        Atlas AI Insurance Opportunity Engine
      </h1>

      <StatsBar
        hot={hot}
        warm={warm}
        cold={cold}
        total={clients.length}
      />

      {clients.map((client) => (
        <ClientCard
          key={client.client_id}
          client={client}
        />
      ))}
    </div>
  );
}