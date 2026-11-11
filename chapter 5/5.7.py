def test_payment_service_uses_stripe_client():
    service = PaymentService()
    assert isinstance(service.gateway, StripeGatewayClient)
    assert service.gateway.api_version == "2023-10-16"
