// Simple requirement: format prices for EUR and USD
export function formatPrice(amount: number, currency: "EUR" | "USD"): string {
  const symbol = currency === "EUR" ? "€" : "$";
  return `${symbol}${amount.toFixed(2)}`;
}

// Contrast this with a future-proofed abstraction created in anticipation of broader needs:

//  future-proof abstraction
interface MoneyFormatter {
  format(amount: number, currency: string): string;
}

class IntlFormatter implements MoneyFormatter {
  constructor(private locale: string) {}
  format(amount: number, currency: string): string {
    return new Intl.NumberFormat(this.locale, {
      style: "currency",
      currency,
    }).format(amount);
  }
}
