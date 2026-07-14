from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.client import Client
from app.models.event import Event

from app.services.opportunity_service import build_opportunities

router = APIRouter()


# -----------------------------
# MAIN ENDPOINT
# -----------------------------
@router.get("/opportunities")
def get_opportunities(db: Session = Depends(get_db)):
    return build_opportunities(db)


# -----------------------------
# DEBUG ENDPOINT
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