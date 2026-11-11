HIGH_VALUE_THRESHOLD = 5000

def notify_order_confirmed(order):
    subject = f"Order #{order.id} confirmed"
    body = f"Hi {order.customer_name}, your order of {order.total} has shipped."

    smtp.send_mail(
        to=order.customer_email,
        subject=subject,
        body=body,
    )

    if order.total >= HIGH_VALUE_THRESHOLD:
        sms.send(
            to=order.warehouse_manager_phone,
            message=f"High-value order #{order.id} ({order.total}) confirmed. Expedite.",
        )

    order.mark_notified()
