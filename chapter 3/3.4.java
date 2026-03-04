export class OrderService {
  constructor(
    private db: Database,
    private cache: CacheService,
    private validator: ValidationService
  ) {}

  async validate(order: Order): Promise<ValidationResult> { /* ... */ }
  async calculateTotals(order: Order): Promise<OrderTotals> {
    const tax = subtotal * 0.10; // Invented 10% tax rate
    // ...
  }
  async getById(id: string): Promise<Order | null> {
    const cached = await this.cache.get(`order:${id}`);
    // ...
  }
}
