import products
import store

# Initial setup of inventory and store
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = store.Store(product_list)


def print_menu():
    """Display the main menu options.Display the main menu options."""
    print("""
        Best Buy Shop
-----------------------------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
""")


def print_products_stock(shop):
    """Display all active products available in the store."""
    print("----- Products in stock -----")
    shop_products = shop.get_all_products()
    for index, product in enumerate(shop_products, start=1):
        print(f"{index}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
    print("-" * 29)


def print_quantity(shop):
    """Display the total quantity of products in the store."""
    print("----- Total stock amount -----")
    products_quantity = shop.get_total_quantity()
    print(f"Total quantity: {products_quantity} products")


def make_order(shop):
    """
    Allow the user to create and process an order.
    The user selects products and quantities until the order is completed.
    """
    print_products_stock(shop)
    print("When you want to finish the order, press Enter without typing anything.")
    total_shopping = 0
    active_products = shop.get_all_products()

    while True:
        # Ask for product number
        product_choice = input("Enter the product number you want to buy: ").strip()
        if product_choice == "":
            break
        if not product_choice.isdigit() or not 1 <= int(product_choice) <= len(active_products):
            print("Error selecting product! Invalid option.")
            continue
        # Ask for amount
        amount_choice = input("Enter the product amount you want to buy: ").strip()
        if amount_choice == "":
            break
        if not amount_choice.isdigit():
            print("Error adding quantity! Must be a number.")
            continue
        # Order product in store
        selected_product = active_products[int(product_choice) - 1]
        selected_quantity = int(amount_choice)
        cost_items = shop.order([(selected_product, selected_quantity)])
        if cost_items:
            total_shopping += cost_items
            print(f"Added {selected_product.name} x {selected_quantity} to your cart!\n")
    print(f"Order processed successfully! Total payment: {total_shopping}$")


def start(shop):
    """Start the Best Buy application.
    Displays the main menu and handles user interaction."""
    router = {
        "1": print_products_stock,
        "2": print_quantity,
        "3": make_order
    }
    print("Welcome to the Best Buy Shop!")
    while True:
        print_menu()
        user_choice = input("Enter your choice [1-4]: ").strip()
        print("")
        if user_choice == "4":
            print("Thanks for visiting!")
            break
        if user_choice in router:
            router[user_choice](shop)
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    start(best_buy)
