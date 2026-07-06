import random
from app.simulator.event_types import EVENT_TYPES


def generate_events(client):

    events = []

    # -----------------------------
    # 1. LATENT INTENT (CRITICAL FIX)
    # -----------------------------
    # only a small % of users are actually "insurance-interested"
    insurance_intent = random.random() < 0.12  # 12% real intent users

    # -----------------------------
    # 2. BASE ACTIVITY (NOISE)
    # -----------------------------
    activity_level = random.uniform(0.3, 0.8)
    num_noise_events = int(activity_level * 10)

    for _ in range(num_noise_events):
        event = random.choice(EVENT_TYPES)
        events.append({
            "client_id": None,
            "event": event
        })

    # -----------------------------
    # 3. INTENT-DRIVEN EVENTS (CORRELATED)
    # -----------------------------
    if insurance_intent and random.random() < 0.6:

        # stronger users generate more meaningful signals
        if random.random() < 0.4:
            events.append({"client_id": None, "event": "insurance_page_view"})

        if random.random() < 0.25:
            events.append({"client_id": None, "event": "term_insurance_view"})

        if random.random() < 0.4:
            events.append({"client_id": None, "event": "search_insurance"})

        if random.random() < 0.3:
            events.append({"client_id": None, "event": "child_plan_calculator"})

        if random.random() < 0.35:
            events.append({"client_id": None, "event": "add_nominee"})

    # -----------------------------
    # 4. LIFE TRIGGERS (WEIGHTED)
    # -----------------------------
    if client["age"] > 30 and random.random() < 0.25:
        events.append({"client_id": None, "event": "insurance_page_view"})

    if client["married"] and random.random() < 0.30:
        events.append({"client_id": None, "event": "add_nominee"})

    if client["children"] > 0 and random.random() < 0.35:
        events.append({"client_id": None, "event": "child_plan_calculator"})

    if client["salary"] > 1500000 and random.random() < 0.20:
        events.append({"client_id": None, "event": "sip_increase"})

    return events