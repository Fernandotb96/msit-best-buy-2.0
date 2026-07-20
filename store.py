from products import Product


class Store:
    """
    Represents a store containing a collection of products.
    Provides methods to manage products and process customer order.
    """
    def __init__(self, products_list=None):
        if products_list is None:
            self.products_list = []
        else:
            if not isinstance(products_list, list):
                raise ValueError("List of products must be a list.")
            if not all(isinstance(p, Product) for p in products_list):
                raise ValueError("All elements in the list must be Product instances.")
            self.products_list = products_list

    def add_product(self, product):
        """Add a product to the store"""
        if not isinstance(product, Product):
            print("Invalid! Must be an instance of Product.")
            return
        if product in self.products_list:
            print(f"Product '{product.name}' is already in the store.")
            return
        self.products_list.append(product)

    def remove_product(self, product):
        """ Remove a product from the store."""
        if product in self.products_list:
            self.products_list.remove(product)
        else:
            print(f"Product {product.name} not in store.")

    def get_total_quantity(self):
        """ Return the total quantity of all products in the store."""
        return sum(product.get_quantity() for product in self.products_list)

    def get_all_products(self):
        """Return a list of all active products in the store."""
        return [product for product in self.products_list if product.is_active()]

    def order(self, shopping_cart):
        """
        Process a customer order returning the final price.
        The shopping cart is a list holding tuples (product, quantity).
        """
        total_price = 0
        for product, requested_quantity in shopping_cart:
            if product in self.products_list:
                total_price += product.buy(requested_quantity)
            else:
                print(f"Error: Product {product.name} not in store.")
        return total_price
