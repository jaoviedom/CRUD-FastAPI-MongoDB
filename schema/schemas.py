def individual_serial(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "age": user.get("age", None),
        "status": user.get("status", "Pending")
    }

def list_serial(users) -> list:
    return[individual_serial(user) for user in users]