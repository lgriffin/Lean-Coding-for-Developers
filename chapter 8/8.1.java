// Layer 1: Fix the schema
// ALTER TABLE refunds MODIFY COLUMN amount_cents BIGINT;

// Layer 2: Prevent recurrence in CI
// schema_lint.yaml -- fails the build if monetary columns use INTEGER
// rules:
//   - pattern: "amount|price|cost|balance|total"
//     required_type: BIGINT
//     message: "Monetary columns must use BIGINT to avoid overflow"

// Layer 3: Detect approaching limits via observability
public class IntegerBoundaryCheck implements HealthIndicator {
    public Health check() {
        long maxValue = db.query(
            "SELECT MAX(amount_cents) FROM refunds"
        );
        double utilizationPct = (double) maxValue / Long.MAX_VALUE * 100;

        if (utilizationPct > 80) {
            return Health.warn("amount_cents at " + utilizationPct + "% of BIGINT max");
        }
        return Health.healthy();
    }
}
