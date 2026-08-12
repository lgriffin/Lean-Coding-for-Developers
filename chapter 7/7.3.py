def process_order(order):
    # Lines 1-80: Payment validation
    if order.payment_method == 'credit_card':
        if not validate_credit_card(order.card_number):
            raise PaymentError("Invalid card")
        if order.amount > get_credit_limit(order.customer):
            raise PaymentError("Exceeds credit limit")
        # ... 60 more lines ...

    # Lines 81-200: Inventory check
    for item in order.items:
        stock = get_stock_level(item.sku, order.warehouse)
        if stock < item.quantity:
            # ... reservation logic ...
        # ... 100 more lines ...

    # Lines 201-295: Shipping calculation
    base_rate = SHIPPING_RATES[order.destination]
    if order.weight > 50:
        # ... weight surcharge logic ...
    # ... 80 more lines ...

    # Lines 296-370: Tax computation — THE PART YOU NEED TO CHANGE
    tax_rate = get_tax_rate(order.destination, order.customer_type)
    order.tax = order.subtotal * tax_rate  # This is the line you need to modify
    # ... 60 more lines ...

    # Lines 371-500: Email, logging, error handling
    # ... 130 more lines ...
