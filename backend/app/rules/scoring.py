import random

def calculate_score(client, events):

    score = 0
    reasons = []

    event_types = [e.event for e in events]

    # -------------------------
    # DEMOGRAPHIC SIGNALS
    # -------------------------

    if 28 <= client.age <= 40:
        score += 8
        reasons.append("Prime financial planning age")

    if client.salary > 2000000:
        score += 6
        reasons.append("High income segment")

    if client.married:
        score += 5
        reasons.append("Married → family protection")

    if client.children > 0:
        score += 8
        reasons.append("Has children → insurance need")

    if client.sip_amount > 30000:
        score += 6
        reasons.append("Strong investment behavior")

    # -------------------------
    # BEHAVIOR SIGNALS
    # -------------------------

    if "insurance_page_view" in event_types:
        score += 8
        reasons.append("Viewed insurance page")

    if "term_insurance_view" in event_types:
        score += 10
        reasons.append("Viewed term insurance")

    if "child_plan_calculator" in event_types:
        score += 10
        reasons.append("Used child plan calculator")

    if "add_nominee" in event_types:
        score += 6
        reasons.append("Added nominee")

    if "search_insurance" in event_types:
        score += 5
        reasons.append("Searched insurance")

    if "sip_increase" in event_types:
        score += 8
        reasons.append("Increased SIP")

    # -------------------------
    # NORMALIZATION
    # -------------------------

    score = min(score, 80)
    score = (score / 80) * 100
    score += random.uniform(-1.5, 1.5)

    return round(max(0, min(100, score)), 2), reasons