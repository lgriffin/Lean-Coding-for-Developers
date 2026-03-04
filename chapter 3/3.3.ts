export async function getOrder(req: Request, res: Response) {
    const id = req.params.id;
  
    // Invented: Where did this format come from?
    if (!/^[A-Z0-9]{8}$/.test(id)) {
      return res.status(400).json({
        error: "Malformed ID",
        message: "Order ID must be 8 alphanumeric characters"
      });
    }
  
    // Invented: Should cancelled orders return 409?
    if (order.status === "CANCELLED") {
      return res.status(409).json({
        error: "Order cancelled",
        message: "Cannot retrieve cancelled orders"
      });
    }
  
    // Invented: Can orders have zero items?
    if (order.items.length === 0) {
      return res.status(422).json({
        error: "Empty order",
        message: "Order contains no items"
      });
    }
  
    // Invented: Why transform items? Was this in the spec?
    return res.status(200).json({
      items: order.items.map(item => ({
        price: item.unitPrice * item.quantity, // Calculated field
      })),
      // ... 10 more lines of invented structure
    });
  }
  