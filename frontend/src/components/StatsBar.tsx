type Props = {
    hot: number;
    warm: number;
    cold: number;
    total: number;
  };
  
  export default function StatsBar({
    hot,
    warm,
    cold,
    total
  }: Props) {
    const boxStyle = {
      flex: 1,
      padding: "20px",
      borderRadius: "10px",
      color: "white",
      textAlign: "center" as const
    };
  
    return (
      <div
        style={{
          display: "flex",
          gap: "20px",
          marginBottom: "30px"
        }}
      >
        <div style={{ ...boxStyle, background: "#dc2626" }}>
          <h2>{hot}</h2>
          HOT
        </div>
  
        <div style={{ ...boxStyle, background: "#d97706" }}>
          <h2>{warm}</h2>
          WARM
        </div>
  
        <div style={{ ...boxStyle, background: "#16a34a" }}>
          <h2>{cold}</h2>
          COLD
        </div>
  
        <div style={{ ...boxStyle, background: "#2563eb" }}>
          <h2>{total}</h2>
          TOTAL
        </div>
      </div>
    );
  }