import logging

logger = logging.getLogger(__name__)

def process_payment(customer, amount, currency):
    logger.info(f"Processing payment: customer={customer.id}, amount={amount}, currency={currency}")
    # ... existing logic ...
    logger.info(f"Payment status: {status}, confirmation_sent={confirmation_sent}")
    logger.info(f"Timezone used: {timezone}, day_of_week: {day_of_week}")
