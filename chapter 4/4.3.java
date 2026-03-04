public interface PaymentProcessor {
    PaymentResult charge(BigDecimal amount);
}

// Implementation details come later
// Could be DebitCardPaymentProcessor, CreditCardPaymentProcessor, etc.
