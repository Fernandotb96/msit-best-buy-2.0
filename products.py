class Product:
    """
    Represents a product that can be sold in the store.
    A product has a name, price, quantity and an active status.
    """
    def __init__(self, name, price, quantity):
        if not name or not name.strip():
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.name = name
        self.price = price
        self.quantity = quantity
        if self.quantity > 0:
            self.active = True
        else:
            self.active = False

    def show(self):
        """Print the product information."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def activate(self):
        """Mark the product as active."""
        self.active = True

    def deactivate(self):
        """Mark the product as inactive."""
        self.active = False

    def is_active(self):
        """Return whether the product is currently active."""
        return self.active

    def get_quantity(self):
        """Return the current quantity of the product in stock."""
        return self.quantity

    def set_quantity(self, quantity):
        """Add or remove units from the stock and updates the status if no more units in stock."""
        self.quantity += quantity
        if self.quantity <= 0:
            self.deactivate()
        else:
            self.activate()

    def buy(self, requested_quantity):
        """
        Purchase a given quantity of the product. Reduces the available stock
        if enough units exist and returns the total price of the purchase.
        """
        if not isinstance(requested_quantity, int) or requested_quantity <= 0:
            print("Invalid quantity! Must be a positive integer.")
            return 0.0
        if not self.is_active():
            print("Product inactive or out of stock!")
            return 0.0
        if requested_quantity > self.quantity:
            print(f"Not enough products in store, only {self.quantity} in stock.")
            return 0.0
        self.set_quantity(-requested_quantity)
        return self.price * requested_quantity


class NonStockedProduct(Product):
    """
    Represents a non-physical product (e.g. software license, digital goods)
    where quantity is not tracked, stays at zero, and stock is unlimited.
    """
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)
        self.activate()

    def show(self):
        """Print the product information."""
        print(f"{self.name}, Price: {self.price}, Quantity: Unlimited")

    def set_quantity(self, quantity):
        """Non-stocked products always keep their quantity unchanged to zero."""
        self.quantity = 0

    def buy(self, requested_quantity):
        """
        Purchase a given quantity of the non-stocked product.
        Does not check or modify stock level, since it is unlimited.
        """
        if not isinstance(requested_quantity, int) or requested_quantity <= 0:
            print("Invalid quantity! Must be a positive integer.")
            return 0.0
        if not self.is_active():
            print("Product inactive or out of stock!")
            return 0.0
        return self.price * requested_quantity
