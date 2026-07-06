import random
from app.simulator.event_types import EVENT_TYPES


def generate_events(client):

    events = []

    # base activity level
    activity_level = random.uniform(0.3, 1.0)

    num_events = int(activity_level * 20)

    for _ in range(num_events):

        event = random.choice(EVENT_TYPES)

        events.append({
            "client_id": None,
            "event": event
        })

    # Add “life triggers” based on profile

    if client["age"] > 30 and random.random() > 0.6:
        events.append({"client_id": None, "event": "insurance_page_view"})

    if client["married"] and random.random() > 0.5:
        events.append({"client_id": None, "event": "add_nominee"})

    if client["children"] > 0 and random.random() > 0.5:
        events.append({"client_id": None, "event": "child_plan_calculator"})

    if client["salary"] > 1000000 and random.random() > 0.6:
        events.append({"client_id": None, "event": "sip_increase"})

    return events