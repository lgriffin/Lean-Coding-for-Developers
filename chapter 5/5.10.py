def test_declined_payment_does_not_reserve_inventory():
    mock_gateway.decline()
    result = service.process(valid_order)

    assert result == "failed"
    assert not inventory.is_reserved(valid_order)
