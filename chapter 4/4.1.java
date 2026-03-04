test('processPayment returns transaction ID when amount is positive', () => {
  const result = processPayment(100);
  expect(result).toMatch(/^txn_/);
});
