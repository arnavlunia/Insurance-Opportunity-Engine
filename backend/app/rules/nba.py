def next_best_action(client, segment):

    if segment == "HOT":
        return {
            "action": "CALL_IMMEDIATELY",
            "product": "Term Insurance + Health Insurance",
            "message": "High intent user — prioritize today."
        }

    elif segment == "WARM":
        return {
            "action": "SEND_WHATSAPP",
            "product": "Child Plan / Retirement Plan",
            "message": "Warm lead — nurture with content."
        }

    return {
        "action": "MONITOR",
        "product": "-",
        "message": "No immediate outreach required."
    }