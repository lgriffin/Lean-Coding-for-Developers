# Overproduced test (structure/implementation policing)
def test_discount_table_contains_expected_entries():
    assert DISCOUNT_TABLE["gold"] == 0.20
    assert DISCOUNT_TABLE["silver"] == 0.10
    assert DISCOUNT_TABLE["basic"] == 0.00

def test_calculate_discount_uses_discount_table():
    # This style shows up a lot in AI output: it “pins” the implementation.
    import inspect
    src = inspect.getsource(calculate_discount)
    assert "DISCOUNT_TABLE" in src
