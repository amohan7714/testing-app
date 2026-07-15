from app import calculate_discount, calculate_order_total, calculate_tax, is_free_shipping


def test_calculate_discount_reduces_price():
    assert calculate_discount(100, 20) == 80


def test_calculate_tax_uses_percentage():
    assert calculate_tax(80, 10) == 8


def test_order_total_includes_subtotal_and_tax():
    assert calculate_order_total(100, 1, discount_percent=20, tax_percent=10) == 88


def test_order_at_free_shipping_threshold_qualifies():
    assert is_free_shipping(50) is True
