from datetime import datetime

def is_expired(expires_at):
    return datetime.utcnow() > datetime.fromisoformat(expires_at)
