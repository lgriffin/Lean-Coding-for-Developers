HIGH_VALUE_THRESHOLD = 5000

def notify_order_confirmed(order):
    message = format_confirmation(order)
    for channel in channels_for(order):
        channel(order, message)
    order.mark_notified()

def channels_for(order):
    yield send_email
    if order.total >= HIGH_VALUE_THRESHOLD:
        yield send_sms
    if order.customer_has_app:
        yield send_push_notification
    yield send_slack

def format_confirmation(order):
    return {
        "subject": f"Order #{order.id} confirmed",
        "body": f"Order {order.id} for {order.customer_name}, total {order.total}.",
    }
