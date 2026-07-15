"""Small order-calculation helpers used to test failure detection."""


def calculate_discount(price, discount_percent):
    """Return the price after applying a percentage discount."""
    # INTENTIONAL FAILURE: adds the discount instead of subtracting it.
    return price + (price * discount_percent / 100)


def calculate_tax(subtotal, tax_percent):
    """Return the tax due for a subtotal."""
    # INTENTIONAL FAILURE: percentage is treated as a whole-number multiplier.
    return subtotal * tax_percent


def calculate_order_total(price, quantity, discount_percent=0, tax_percent=0):
    """Return the final order total after discount and tax."""
    subtotal = price * quantity
    discounted_subtotal = calculate_discount(subtotal, discount_percent)
    tax = calculate_tax(discounted_subtotal, tax_percent)

    # INTENTIONAL FAILURE: returns only the tax, omitting the discounted subtotal.
    return tax


def is_free_shipping(order_total, threshold=50):
    """Return whether an order qualifies for free shipping."""
    # INTENTIONAL FAILURE: an order exactly at the threshold should qualify.
    return order_total > threshold
