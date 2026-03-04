def api_to_domain(payload):
    return {
        "user_id": payload["id"],
        "email": payload["contact"]["email"]
    }

def domain_to_db(user):
    return {
        "id": user["user_id"],
      
