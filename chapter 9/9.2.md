# What the metric sees
pr_cycle_times = [1.2, 0.8, 1.5, 0.9, 1.1]  # days per PR
avg_cycle = sum(pr_cycle_times) / len(pr_cycle_times)
print(f"Average PR cycle time: {avg_cycle:.1f} days")  # 1.1 days, great!

# What actually happened
feature_lead_time = 14  # days from request to production
prs_per_feature = 5     # artificially split
total_review_overhead = prs_per_feature * 0.5  # hours per PR for context switching

# The metric improved. The system didn't.
# Feature lead time is unchanged. Review overhead increased.
