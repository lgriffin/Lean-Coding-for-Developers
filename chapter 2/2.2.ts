function checkout(user: User) {
    if (process.env.NEW_CHECKOUT === "true") {
      // v2 path: partially rolled out, still missing edge cases
      return newCheckout(user);
    }
  
    // v1 path: still required for most users
    return oldCheckout(user);
  }
  
  // months later: both paths still exist, tests and fixes must consider both
  