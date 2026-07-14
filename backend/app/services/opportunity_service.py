from app.models.client import Client
from app.models.event import Event

from app.services.scoring_service import evaluate_client
from app.rules.nba import next_best_action


def build_opportunities(db):

    clients = db.query(Client).all()

    results = []

    # -----------------------------
    # Score every client
    # -----------------------------
    for client in clients:

        events = (
            db.query(Event)
            .filter(Event.client_id == client.id)
            .all()
        )

        result = evaluate_client(client, events)

        result["name"] = client.name

        results.append(result)

    # -----------------------------
    # Rank by score
    # -----------------------------
    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    total = len(results)

    hot_cutoff = max(1, int(total * 0.10))
    warm_cutoff = max(hot_cutoff + 1, int(total * 0.30))

    # -----------------------------
    # Assign segments
    # -----------------------------
    for i, client in enumerate(results):

        if i < hot_cutoff:
            client["segment"] = "HOT"

        elif i < warm_cutoff:
            client["segment"] = "WARM"

        else:
            client["segment"] = "COLD"

        client["next_best_action"] = next_best_action(
            client,
            client["segment"]
        )

    return results