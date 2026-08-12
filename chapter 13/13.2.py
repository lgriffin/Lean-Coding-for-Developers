def test_refund_exceeding_original_amount_is_rejected():
    order = create_order(amount_cents=5000)
    result = process_refund(order, refund_cents=5001)
    assert result.status == "REJECTED"
    assert result.reason == "Refund exceeds original transaction amount"

def test_partial_refund_reduces_remaining_refundable_amount():
    order = create_order(amount_cents=5000)
    process_refund(order, refund_cents=2000)
    result = process_refund(order, refund_cents=3001)
    assert result.status == "REJECTED"
    assert result.reason == "Refund exceeds remaining refundable amount"
