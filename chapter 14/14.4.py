# report_generator.py - written two months ago
def generate_monthly_report(tenant_id: str) -> bytes:
    transactions = db.fetch_all_transactions(tenant_id)  # loads ALL into memory
    report_rows = [format_row(t) for t in transactions]
    csv_content = "\n".join(report_rows)
    return csv_content.encode("utf-8")
