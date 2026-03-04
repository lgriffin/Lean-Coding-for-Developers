def test_shipping_cost_for_domestic_package_under_5kg():
    assert calculate_shipping(weight=3, destination="domestic") == 5.99
