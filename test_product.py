import pytest
from products import Product


# Test that creating a normal product works.
def test_create_normal_product():
    """Test that creating a normal product sets all attributes correctly."""
    product = Product("Asus Expertbook", 750.0, 25)

    assert product.name == "Asus Expertbook"
    assert product.price == 750.0
    assert product.get_quantity() == 25
    assert product.is_active() is True


# Test that creating a product with invalid details (empty name, negative price) invokes an exception.
def test_create_invalid_product():
    """Test that creating a product with empty name or negative value invokes an exception."""
    with pytest.raises(ValueError):
        Product("", 100.0, 5)

    with pytest.raises(ValueError):
        Product("   ", 100.0, 5)

    with pytest.raises(ValueError):
        Product("Mouse", -10.0, 5)

    with pytest.raises(ValueError):
        Product("Mouse", 10.0, -5)


# Test that when a product reaches 0 quantity, it becomes inactive.
def test_product_quantity_zero():
    """Test that when a product's quantity reaches 0, it becomes inactive."""
    mouse = Product("Mouse", 50.0, 1)
    mouse.buy(1)

    assert mouse.get_quantity() == 0
    assert mouse.is_active() is False


# Test that product purchase modifies the quantity and returns the right output.
def test_buy_product():
    """Test that a valid purchase reduces stock and returns the correct total price."""
    monitor = Product("Monitor", 200.0, 10)
    total_price = monitor.buy(3)

    assert total_price == 600.0
    assert monitor.get_quantity() == 7


# Test that buying a larger quantity than exists invokes exception.
def test_buy_too_large_quantity():
    """Test that buying a larger quantity than exists returns 0.0 and leaves stock unchanged."""
    headphones = Product("Headphones", 30.0, 5)
    total_price = headphones.buy(10)

    assert total_price == 0.0
    assert headphones.get_quantity() == 5


# In console: py -m pytest -v
