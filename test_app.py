from app import calculate_discount


def test_calculate_discount_reduces_price():
    assert calculate_discount(100, 20) == 80
