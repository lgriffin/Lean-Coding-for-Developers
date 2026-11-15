from datetime import UTC, datetime

def is_expired(expires_at):
    return datetime.now(tz=UTC) > datetime.fromisoformat(expires_at)
