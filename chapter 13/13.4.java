public record ReservationPlaced(
    ReservationId id,
    FulfilmentCentreId centreId,
    ProductId productId,
    Quantity reserved,
    Instant occurredAt
) implements DomainEvent {

    public ReservationPlaced {
        Objects.requireNonNull(id, "ReservationId must not be null");
        Objects.requireNonNull(centreId, "FulfilmentCentreId must not be null");
        if (reserved.isNegative()) {
            throw new IllegalArgumentException("Reserved quantity must not be negative");
        }
    }
}
