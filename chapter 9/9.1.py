import math
from datetime import datetime

def lead_time_days(request_created: datetime, deployed_at: datetime) -> float:
    """Calendar days from request creation to production deployment."""
    return (deployed_at - request_created).total_seconds() / 86400

def percentile(sorted_values: list, pct: int) -> float:
    """Nearest-rank percentile: the value that pct% of items fall at or below."""
    rank = math.ceil(pct / 100 * len(sorted_values))
    return sorted_values[max(rank - 1, 0)]

def summarize_lead_times(items: list) -> dict:
    """Compute median and percentiles for a set of completed work items."""
    lead_times = sorted(
        lead_time_days(i.created, i.deployed) for i in items
    )
    return {
        "p50": percentile(lead_times, 50),
        "p75": percentile(lead_times, 75),
        "p90": percentile(lead_times, 90),
        "min": lead_times[0],
        "max": lead_times[-1],
    }

items = fetch_completed_items(last_n=20)
stats = summarize_lead_times(items)
print(f"Median lead time: {stats['p50']:.1f} days")
print(f"90th percentile: {stats['p90']:.1f} days")
