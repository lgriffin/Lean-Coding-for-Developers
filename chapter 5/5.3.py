def test_order_expires_after_30_minutes():
    order = create_order()

    advance_time(minutes=30)
    process_expirations()

    assert order.status == "expired"
