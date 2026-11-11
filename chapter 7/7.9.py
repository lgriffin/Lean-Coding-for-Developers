def test_discount_calculation_characterization():
    # Capture actual behavior, even if it seems wrong
    assert calculate_discount(100, 'SUMMER') == 15.0
    assert calculate_discount(0, 'SUMMER') == 0.0
    assert calculate_discount(-50, 'SUMMER') == 0.0  # Bug? Maybe. Current behavior.
    assert calculate_discount(100, 'INVALID') == 0.0
    assert calculate_discount(1000, 'VIP') == 250.0
    assert calculate_discount(999, 'VIP') == 99.9   # Why does threshold matter? Document it.
