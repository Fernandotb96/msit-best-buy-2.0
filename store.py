class Store:
    """
    Represents a store containing a collection of products.
    Provides methods to manage products and process customer order.
    """
    def __init__(self, products_list):
        if products_list is None:
            self.products_list = []
        else:
            self.products_list = products_list

    def add_product(self, product):
        """Add a product to the store"""
        self.products_list.append(product)

    def remove_product(self, product):
        """ Remove a product from the store."""
        if product in self.products_list:
            self.products_list.remove(product)
        else:
            print(f"Product {product.name} not in store.")

    def get_total_quantity(self):
        """ Return the total quantity of all products in the store."""
        total = 0
        for product in self.products_list:
            total += product.quantity
        return total

    def get_all_products(self):
        """Return a list of all active products in the store."""
        active_products = []
        for product in self.products_list:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_cart):
        """
        Process a customer order returning the final price.
        The shopping cart is a list holding tuples (product, quantity).
        """
        total_price = 0
        for product, quantity in shopping_cart:
            if product in self.products_list:
                total_price += product.buy(quantity)
            else:
                print(f"Error, product {product.name} not in store.")
        return total_price
