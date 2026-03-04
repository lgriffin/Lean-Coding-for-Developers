describe('GET /orders/:id', () => {
    it('should return 200 with order details for valid ID', async () => {
      const response = await request(app).get('/orders/123');
      expect(response.status).toBe(200);
      expect(response.body).toHaveProperty('id');
    });
  
    it('should return 404 when order does not exist', async () => {
      const response = await request(app).get('/orders/nonexistent');
      expect(response.status).toBe(404);
    });
  });
  