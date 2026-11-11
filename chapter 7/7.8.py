def process_payment(request):
    if should_use_new_system(request):
        return new_payment_service.process(request)
    else:
        return legacy_payment_system.process(request)

def should_use_new_system(request):
    # Phase 1: Internal test traffic only
    if request.headers.get('X-Internal-Test'):
        return True

    # Phase 2: 1% of production traffic
    if hash(request.user_id) % 100 == 0:
        return True

    # Phase 3: Gradually increase to 10%, 25%, 50%, 100%
    return rollout_percentage_for_user(request.user_id) < CURRENT_ROLLOUT_PCT
