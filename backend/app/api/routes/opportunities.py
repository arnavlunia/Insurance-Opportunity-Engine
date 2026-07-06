from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.client import Client
from app.models.event import Event

from app.services.scoring_service import evaluate_client

router = APIRouter()


# -----------------------------
# MAIN ENDPOINT
# -----------------------------
@router.get("/opportunities")
def get_opportunities(db: Session = Depends(get_db)):

    clients = db.query(Client).all()

    results = []

    for client in clients:

        events = (
            db.query(Event)
            .filter(Event.client_id == client.id)
            .all()
        )

        scored_client = evaluate_client(client, events)

        results.append({
            "client_id": client.id,
            "name": client.name,
            "score": scored_client.get("score", 0),
            "segment": scored_client.get("segment", "low"),
            "reasons": scored_client.get("reasons", []),
            "next_best_action": scored_client.get("next_best_action", {
                "action": "Nurture",
                "product": "N/A",
                "message": "Insufficient signals"
            })
        })

    # Sort by score descending
    results.sort(key=lambda x: x["score"], reverse=True)

    return results


# -----------------------------
# DEBUG ENDPOINT (DATA INSPECTION)
# -----------------------------
@router.get("/debug/opportunities")
def debug_opportunities(db: Session = Depends(get_db)):

    clients = db.query(Client).all()

    raw_data = []

    for client in clients:
        events = (
            db.query(Event)
            .filter(Event.client_id == client.id)
            .all()
        )

        raw_data.append({
            "client": {
                "id": client.id,
                "name": client.name
            },
            "events": [
                {
                    "type": e.event_type,
                    "value": getattr(e, "value", None),
                    "timestamp": str(getattr(e, "timestamp", None))
                }
                for e in events
            ]
        })

    return {
        "total_clients": len(clients),
        "sample": raw_data[:10]
    }