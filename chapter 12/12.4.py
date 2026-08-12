def payment_outage_runbook():
    """Executable runbook: payment processing outage."""
    print("Step 1: Checking payment gateway status...")
    gw_status = check_gateway_health("stripe")
    print(f"  Gateway status: {gw_status}")

    print("Step 2: Checking payment-service error rate...")
    error_rate = get_service_error_rate("payment-service", window="5m")
    print(f"  Error rate: {error_rate:.2%}")

    print("Step 3: Checking database connection pool...")
    pool_usage = get_db_pool_usage("payments-db")
    print(f"  Pool usage: {pool_usage:.0%}")

    if pool_usage > 0.90:
        print("  ACTION: Pool near capacity. Kill idle connections.")
        kill_idle_connections("payments-db", older_than_minutes=10)

    print("Step 4: Checking queue depth...")
    depth = get_queue_depth("payment-processing-queue")
    print(f"  Queue depth: {depth} (normal < 100)")

    if depth > 500:
        print("  ESCALATE: Queue backing up. Page payments team lead.")
        page_oncall("payments-team-lead", "Queue depth critical: {depth}")
