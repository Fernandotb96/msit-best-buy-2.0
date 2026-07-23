from promotions import Promotion


class Product:
    """
    Represents a product that can be sold in the store.
    A product has a name, price, quantity, an active status and, optionally, a promotion applied to it.
    """
    def __init__(self, name, price, quantity):
        if not name or not name.strip():
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.name = name
        self._price = price
        self._quantity = quantity
        self.promotion = None
        if self.quantity > 0:
            self.active = True
        else:
            self.active = False

    def __str__(self):
        promotion_text = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: ${self.price} Quantity: {self.quantity}{promotion_text}"

    def __gt__(self, other):
        if not isinstance(other, Product):
            raise TypeError(f"{other} is not an instance of Product.")
        return self.price > other.price

    def __lt__(self, other):
        if not isinstance(other, Product):
            raise TypeError(f"{other} is not an instance of Product.")
        return self.price < other.price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self._price = new_price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity):
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = new_quantity
        if self._quantity <= 0:
            self.deactivate()
        else:
            self.activate()

    def activate(self):
        """Mark the product as active."""
        self.active = True

    def deactivate(self):
        """Mark the product as inactive."""
        self.active = False

    def is_active(self):
        """Return whether the product is currently active."""
        return self.active

    def get_promotion(self):
        """Return the promotion currently applied to this product, or None."""
        return self.promotion

    def set_promotion(self, promotion):
        """Set (or remove, passing None) the promotion applied to this product."""
        if promotion is not None and not isinstance(promotion, Promotion):
            raise ValueError("Promotion must be an instance of Promotion (or None).")
        self.promotion = promotion

    def get_final_price(self, quantity):
        """
        Return the total price for buying `quantity` units, applying the
        current promotion if one is set, otherwise the regular price.
        """
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity

    def buy(self, requested_quantity):
        """
        Purchase a given quantity of the product. Reduces the available stock
        if enough units exist and returns the total price of the purchase,
        applying the product's promotion (if any) via get_price().
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
        self.quantity -= requested_quantity
        return self.get_final_price(requested_quantity)


class NonStockedProduct(Product):
    """
    Represents a non-physical product (e.g. software license, digital goods)
    where quantity is not tracked, stays at zero, and stock is unlimited.
    """
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)
        self.activate()

    def __str__(self):
        promotion_text = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: ${self.price} Quantity: Unlimited{promotion_text}"

    @property
    def quantity(self):
        """Always zero: non-stocked products have unlimited, untracked stock."""
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        """Non-stocked products ignore quantity changes; quantity always stays at zero."""
        self._quantity = 0

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
        return self.get_final_price(requested_quantity)


class LimitedProduct(Product):
    """
    Represents a product that can only be purchased up to a maximum quantity per order
    (e.g., shipping fee, limited edition items, promotional items).
    """
    def __init__(self, name, price, quantity, maximum):
        if not isinstance(maximum, int) or maximum <= 0:
            raise ValueError("Maximum quantity must be a positive integer.")
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def __str__(self):
        promotion_text = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return (f"{self.name}, Price: ${self.price} Quantity:{self.quantity}, "
                f"Limited to {self.maximum} per order{promotion_text}")

    def buy(self, requested_quantity):
        """Purchase a given quantity of the product, only up to the maximum allowed per order."""
        if requested_quantity > self.maximum:
            raise ValueError(f"Product '{self.name}' can only be purchased up to {self.maximum} time(s) per order.")
        return super().buy(requested_quantity)
