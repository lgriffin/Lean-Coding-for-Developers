# Production code
DISCOUNT_TABLE = {
    "gold": 0.20,
    "silver": 0.10,
    "basic": 0.00,
}

def calculate_discount(price: float, tier: str) -> float:
    return price * DISCOUNT_TABLE.get(tier, 0.0)
