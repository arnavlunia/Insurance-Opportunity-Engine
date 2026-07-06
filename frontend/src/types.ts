export interface NextBestAction {
    action: string;
    product: string | null;
    message: string;
  }
  
  export interface Opportunity {
    client_id: number;
    name: string;
    score: number;
    segment: "HOT" | "WARM" | "COLD";
    reasons: string[];
    next_best_action: NextBestAction;
  }