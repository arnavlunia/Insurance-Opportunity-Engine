import math
import random

def calculate_score(client, events):

    score = 0.0
    reasons = []

    event_types = [e.event for e in events]

    # -------------------------
    # BASE SIGNALS (0–60 range max)
    # -------------------------

    if 28 <= client.age <= 40:
        score += 8
        reasons.append("Prime financial planning age")

    if client.salary > 1000000:
        score += 10
        reasons.append("High income segment")

    if client.married:
        score += 6
        reasons.append("Married → family protection need")

    if client.children > 0:
        score += 10
        reasons.append("Has children → insurance need")

    if client.sip_amount > 20000:
        score += 8
        reasons.append("Strong investment behavior")

    # -------------------------
    # BEHAVIOR SIGNALS (HIGH IMPACT)
    # -------------------------

    if "insurance_page_view" in event_types:
        score += 12
        reasons.append("Viewed insurance page")

    if "term_insurance_view" in event_types:
        score += 15
        reasons.append("Viewed term insurance")

    if "child_plan_calculator" in event_types:
        score += 12
        reasons.append("Used child plan calculator")

    if "add_nominee" in event_types:
        score += 10
        reasons.append("Added nominee")

    if "search_insurance" in event_types:
        score += 8
        reasons.append("Searched insurance")

    # -------------------------
    # NORMALIZATION (IMPORTANT FIX)
    # -------------------------

    # convert to probability space
    score = score / 80.0   # max theoretical ~80

    # sigmoid compression (VERY IMPORTANT)
    score = 1 / (1 + math.exp(-8 * (score - 0.5)))

    # scale to 0–100
    score = score * 100

    # -------------------------
    # SMALL NOISE (NOT DESTROYING RANKING)
    # -------------------------

    score += random.uniform(-2, 2)

    # clamp
    score = max(0, min(100, score))

    return round(score, 2), reasons