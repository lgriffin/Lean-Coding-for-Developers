MAX_RETRY_ATTEMPTS = 3
BACKOFF_BASE_SECONDS = 2

def process_refund(refund_request: RefundRequest) -> RefundResult:
    """Apply refund to the original payment method.

    Retries on transient gateway errors. Fails loudly on
    business rule violations so the caller can route to manual review.
    """
    validate_refund_rules(refund_request)
    for attempt in range(MAX_RETRY_ATTEMPTS):
        result = gateway.submit(refund_request)
        if result.is_transient_error():
            sleep(BACKOFF_BASE_SECONDS ** attempt)
            continue
        return result
    raise RefundGatewayTimeout(refund_request.id, MAX_RETRY_ATTEMPTS)
