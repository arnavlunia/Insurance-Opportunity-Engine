from app.db.session import SessionLocal

from app.models.client import Client
from app.models.event import Event

from app.simulator.client_generator import generate_client
from app.simulator.behavior_engine import generate_events


def run_seed(n=100):

    db = SessionLocal()

    for _ in range(n):

        client_data = generate_client()

        client = Client(**client_data)

        db.add(client)
        db.commit()
        db.refresh(client)

        events = generate_events(client_data)

        for e in events:

            event = Event(
                client_id=client.id,
                event=e["event"]
            )

            db.add(event)

        db.commit()

    db.close()

    print(f"Seeded {n} clients successfully")