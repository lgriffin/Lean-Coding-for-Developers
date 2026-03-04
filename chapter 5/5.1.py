# Waste: tests implementation details
def test_payment_uses_token_bucket_limiter():
    processor = PaymentProcessor()
    processor.process(payment_request)
    assert isinstance(processor.limiter, TokenBucketRateLimiter)
    assert processor.limiter.calls == [call(rate=100, burst=10)]

# Value: tests behavior
def test_payment_respects_rate_limits():
    processor = PaymentProcessor()
    results = [processor.process(payment_request) for _ in range(150)]
    
    passed = sum(1 for r in results if r.success)
    rate_limited = sum(1 for r in results if r.rate_limited)
    
    assert passed <= 110  # allows burst
    assert rate_limited >= 40
