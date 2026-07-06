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
  
  export default function ClientCard({ client }: { client: Client }) {
    const badgeColor =
      client.segment === "HOT"
        ? "#ef4444"
        : client.segment === "WARM"
        ? "#f59e0b"
        : "#22c55e";
  
    return (
      <div
        style={{
          background: "#ffffff",
          borderRadius: "12px",
          padding: "20px",
          marginBottom: "18px",
          boxShadow: "0 3px 10px rgba(0,0,0,0.08)"
        }}
      >
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center"
          }}
        >
          <div>
            <h2>{client.name}</h2>
            <p>Score: <b>{client.score}</b></p>
          </div>
  
          <span
            style={{
              background: badgeColor,
              color: "white",
              padding: "6px 12px",
              borderRadius: "8px",
              fontWeight: "bold"
            }}
          >
            {client.segment}
          </span>
        </div>
  
        <hr />
  
        <h4>Why?</h4>
  
        <ul>
          {client.reasons.map((reason, index) => (
            <li key={index}>{reason}</li>
          ))}
        </ul>
  
        <hr />
  
        <h4>Next Best Action</h4>
  
        <p>
          <b>{client.next_best_action.action}</b>
        </p>
  
        <p>{client.next_best_action.product}</p>
  
        <p>{client.next_best_action.message}</p>
      </div>
    );
  }