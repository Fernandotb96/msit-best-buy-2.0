class Product:
    """
    Represents a product that can be sold in the store.
    A product has a name, price, quantity and an active status.
    """
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """Return the current quantity of the product in stock."""
        return self.quantity

    def activate(self):
        """Mark the product as active."""
        self.active = True

    def deactivate(self):
        """Mark the product as inactive."""
        self.active = False

    def add_quantity(self, quantity):
        """Add or remove units from the stock and updates the status if no more units in stock."""
        self.quantity += quantity
        if self.quantity <= 0:
            self.deactivate()
        else:
            self.activate()

    def is_active(self):
        """Return whether the product is currently active."""
        return self.active

    def show(self):
        """Print the product information."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        """
        Purchase a given quantity of the product. Reduces the available stock
        if enough units exist and returns the total price of the purchase.
        """
        if self.quantity >= quantity:
            self.add_quantity(-quantity)
            return self.price * quantity
        if not self.is_active():
            print("Product out of stock!")
            return 0.0
        print(f"Not enough products in store, only {self.quantity} in stock.")
        return 0.0
