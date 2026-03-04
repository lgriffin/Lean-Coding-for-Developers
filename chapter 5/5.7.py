def test_payment_rejects_invalid_amounts():
    result = process_payment(amount=-10, card="4111111111111111")
    assert result.status == "rejected"
    assert result.error == "Invalid payment amount"

def test_declined_payment_does_not_reserve_inventory():
    mock_gateway.configure_to_decline()
    result = process_payment(amount=100, card="4111111111111111")

    assert result.status == "failed"
    assert inventory.reserved_count() == 0
