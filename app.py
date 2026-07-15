def calculate_discount(price, discount_percent):
    """Return the discounted price."""
    # Intentional bug for CI/root-cause testing:
    # this adds the discount instead of subtracting it.
    return price + (price * discount_percent / 100)
