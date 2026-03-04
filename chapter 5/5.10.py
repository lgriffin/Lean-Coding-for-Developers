def test_invalid_amount_raises():
    with pytest.raises(ValueError):
        service.process(order_with_zero_amount)

def test_success_path_executes():
    mock_gateway.approve()
    result = service.process(valid_order)
    assert result == "success"
