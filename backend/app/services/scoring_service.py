from app.rules.scoring import calculate_score


def evaluate_client(client, events):

    score, reasons = calculate_score(client, events)

    return {
        "client_id": client.id,
        "score": score,
        "reasons": reasons
    }