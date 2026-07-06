def next_best_action(client, score):

    if score >= 75:
        return {
            "action": "CALL_IMMEDIATELY",
            "product": "Term Insurance + Health Insurance",
            "message": "High intent user — prioritize call today"
        }

    elif score >= 50:
        return {
            "action": "SEND_WHATSAPP",
            "product": "Child Plan / Retirement Plan",
            "message": "Warm lead — nurture with content"
        }

    else:
        return {
            "action": "MONITOR",
            "product": None,
            "message": "Low intent — no action needed"
        }