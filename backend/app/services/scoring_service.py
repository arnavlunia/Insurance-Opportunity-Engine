from app.rules.scoring import calculate_score
from app.rules.segmentation import segment
from app.rules.nba import next_best_action


def evaluate_client(client, events):

    score, reasons = calculate_score(client, events)

    segment_label = segment(score)

    nba = next_best_action(client, score)

    return {
        "client_id": client.id,
        "score": score,
        "segment": segment_label,
        "reasons": reasons,
        "next_best_action": nba
    }