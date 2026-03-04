def test_gold_users_receive_twenty_percent_discount():
    assert calculate_discount(200, "gold") == 40
