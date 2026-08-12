# report_generator.py - streaming version
def generate_monthly_report(tenant_id: str) -> Iterator[bytes]:
    for batch in db.fetch_transactions_batched(tenant_id, batch_size=1000):
        for transaction in batch:
            yield format_row(transaction).encode("utf-8")
            yield b"\n"
