def build_opportunities(db):
    clients = db.query(Client).all()

    results = []

    for client in clients:
        events = db.query(Event).filter(Event.client_id == client.id).all()
        result = evaluate_client(client, events)

        result["name"] = client.name
        results.append(result)

    return sorted(results, key=lambda x: x["score"], reverse=True)