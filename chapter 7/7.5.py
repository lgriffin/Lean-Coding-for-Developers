def notify_order_confirmed(order):
    subject = f"Order #{order.id} confirmed"
    body = f"Hi {order.customer_name}, your order of {order.total} has shipped."
    smtp.send_mail(
        to=order.customer_email,
        subject=subject,
        body=body,
    )
    order.mark_notified()
