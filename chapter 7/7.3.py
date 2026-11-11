def process_order(order):
    validate_payment(order)
    reserve_inventory(order)
    calculate_shipping(order)
    calculate_tax(order)  # Only this function changes for tax updates
    send_confirmation(order)
    log_order_processed(order)

def calculate_tax(order):
    # 30 lines of focused tax logic
    tax_rate = get_tax_rate(order.destination, order.customer_type)
    order.tax = order.subtotal * tax_rate
    return order.tax
