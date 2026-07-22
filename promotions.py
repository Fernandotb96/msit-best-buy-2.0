from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract base class for all promotions.

    A promotion has a name and knows how to calculate the total price
    for a given product and quantity once the discount is applied.
    It cannot be instantiated directly - every promotion must be one
    of the concrete types below (PercentDiscount, SecondHalfPrice, ThirdOneFree).
    """
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Return the total price (float) for buying `quantity` units of
        `product`, after this promotion has been applied.
        """
        pass


class PercentDiscount(Promotion):
    """Apply a fixed percentage discount to the whole purchase (e.g. 20% off)."""
    def __init__(self, name, percent):
        super().__init__(name)
        if not 0 <= percent <= 100:
            raise ValueError("Percent must be between 0 and 100.")
        self.percent = percent

    def apply_promotion(self, product, quantity):
        total_price = product.price * quantity
        discount = total_price * (self.percent / 100)
        return total_price - discount


class SecondHalfPrice(Promotion):
    """Every second unit purchased is sold at half price."""
    def apply_promotion(self, product, quantity):
        half_price_units = quantity // 2
        full_price_units = quantity - half_price_units
        return (full_price_units * product.price) + (half_price_units * (product.price / 2))


class ThirdOneFree(Promotion):
    """For every 3 units purchased, one of them is free (Buy 2, get 1 free)."""
    def apply_promotion(self, product, quantity):
        free_units = quantity // 3
        paid_units = quantity - free_units
        return paid_units * product.price
