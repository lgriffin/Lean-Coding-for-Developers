def post_deploy_monitor(deploy_id: str, baseline_error_rate: float):
    """Watch error rate for 10 minutes after deploy. Rollback if it spikes."""
    for minute in range(10):
        current_rate = get_error_rate(window_minutes=1)
        if current_rate > baseline_error_rate * 3:
            trigger_rollback(deploy_id)
            notify_team(
                f"Auto-rollback: deploy {deploy_id}. "
                f"Error rate {current_rate:.2%} vs baseline {baseline_error_rate:.2%}"
            )
            return "rolled_back"
        time.sleep(60)
    return "stable"
