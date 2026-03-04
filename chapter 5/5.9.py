class PaymentService:
    def process(self, order):
        if order.amount <= 0:
            raise ValueError("Invalid amount")

        if not self.gateway.charge(order):
            return "failed"

        self.inventory.reserve(order)
        self.email.send_confirmation(order)

        return "success"
