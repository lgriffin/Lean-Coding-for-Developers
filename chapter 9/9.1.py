from datetime import datetime

def lead_time_days(request_created: datetime, deployed_at: datetime) -> float:
    """Calendar days from request creation to production deployment."""
    return (deployed_at - request_created).total_seconds() / 86400

def summarize_lead_times(items: list) -> dict:
    """Compute median and percentiles for a set of completed work items."""
    lead_times = sorted(
        lead_time_days(i.created, i.deployed) for i in items
    )
    n = len(lead_times)
    return {
        "p50": lead_times[n // 2],
        "p75": lead_times[int(n * 0.75)],
        "p90": lead_times[int(n * 0.90)],
        "min": lead_times[0],
        "max": lead_times[-1],
    }

items = fetch_completed_items(last_n=20)
stats = summarize_lead_times(items)
print(f"Median lead time: {stats['p50']:.1f} days")
print(f"90th percentile: {stats['p90']:.1f} days")
