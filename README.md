# Best Buy Store — Part 2

A command-line store simulation built in Python. This is the **second part** of the
"Best Buy" project, developed for the MSIT programming course. Part 2 builds on
Part 1 to go deeper into **Object-Oriented Programming (OOP)** concepts: abstract
classes, inheritance, magic methods, and properties.

## About the project

The program simulates a simple electronics shop. A user can browse the available
products, check the total stock, and place an order through a text menu in the
terminal. Behind the scenes, the project is organized around a small set of
classes that model products, promotions, and the store itself.

## What's new in Part 2

Compared to Part 1, this version adds:

- **Promotions system** (`promotions.py`): an abstract `Promotion` base class
  (built with Python's `abc` module) with three concrete promotions:
  - `PercentDiscount` — applies a percentage discount to the total.
  - `SecondHalfPrice` — every second unit is sold at half price.
  - `ThirdOneFree` — for every 3 units bought, 1 is free.
- **Properties instead of getters/setters**: `price`, `quantity`, and `promotion`
  on `Product` are now managed with `@property` / `@setter`, with validation
  built into the setters (e.g. price/quantity can't be negative).
- **Magic methods**:
  - `__str__` on `Product` and `Store`-related classes, so `print(product)`
    shows a readable description instead of needing a separate `show()` method.
  - `__gt__` / `__lt__` on `Product`, to compare two products by price.
  - `__contains__` on `Store`, so you can write `if product in store`.
  - `__add__` on `Store`, so two stores can be merged with `store1 + store2`.
- **New product types** (`products.py`):
  - `NonStockedProduct` — for digital goods with unlimited stock (e.g. a
    software license). Quantity is always 0 and never tracked.
  - `LimitedProduct` — for products that can only be bought up to a maximum
    quantity per order (e.g. a shipping fee).
- **Order flow fix**: orders are now collected into a cart and processed in a
  single call to `Store.order()`, instead of buying items one by one. This
  prevents a bug where a `LimitedProduct`'s per-order limit could be bypassed
  by adding it to the cart multiple times.

## Project structure

```
best-buy-store/
├── main.py            # Entry point: menu, user interaction, order flow
├── products.py         # Product, NonStockedProduct, LimitedProduct classes
├── store.py            # Store class: manages the product catalog
├── promotions.py        # Promotion (abstract) and concrete promotion classes
├── test_product.py      # Unit tests for the Product class (pytest)
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.8 or higher
- The application itself has no external dependencies — it only uses the
  Python standard library (`abc` module for the abstract `Promotion` class).
- [`pytest`](https://docs.pytest.org/) is required only to run the unit tests
  in `test_product.py`. It's listed in `requirements.txt`.

## Installation

1. Clone or download the project.
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS / Linux
   venv\Scripts\activate         # Windows
   ```
3. Install dependencies (there are none right now, but this keeps the setup
   consistent for future additions):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the program from the project folder:

```bash
python main.py
```

You'll see a menu with the following options:

```
Best Buy Shop
-----------------------------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
```

- **Option 1** shows all active products currently available.
- **Option 2** shows the total quantity of stocked products.
- **Option 3** lets you build an order by selecting a product and a quantity,
  repeated as many times as you like. Press Enter without typing anything to
  finish the order.
- **Option 4** exits the program.

## Testing

The project includes a small suite of unit tests (`test_product.py`) written
with [`pytest`](https://docs.pytest.org/), which check the behavior of the
`Product` class in isolation, without going through the menu.

To run the tests, from the project folder:

```bash
pytest test_product.py
```

or simply `pytest` to run every test file in the project.

The tests currently cover:

- **Creating a valid product** — checks that `name`, `price`, `quantity`, and
  `is_active()` are set correctly.
- **Creating an invalid product** — checks that a `ValueError` is raised for
  an empty/blank name, a negative price, or a negative quantity.
- **Quantity reaching zero** — checks that a product automatically becomes
  inactive (`is_active()` returns `False`) once its stock hits 0.
- **A valid purchase** — checks that `buy()` returns the correct total price
  and reduces the stock by the right amount.
- **Buying more than the available stock** — checks that `buy()` returns
  `0.0` and leaves the stock unchanged, instead of allowing an overselling
  purchase.

Writing these tests was a good exercise to see how to check both the "happy
path" (valid inputs) and the edge cases (invalid inputs, insufficient stock)
of a class, using `pytest.raises` for the cases that are expected to throw
an exception.

## A few design decisions worth noting

- **`__eq__` is intentionally not implemented on `Product`.** The store keeps
  using the default identity-based equality, since `add_product`,
  `remove_product`, and `order` rely on comparing the *exact same object*,
  not just two products with matching attributes.
- **`NonStockedProduct` is excluded from `Store.get_total_quantity()`**, since
  its stock is unlimited and doesn't represent physical quantity in the store.
- **Cart-then-order pattern**: `make_order()` collects all selections into a
  dictionary first, and only calls `Store.order()` once at the end. This makes
  it possible to correctly enforce limits like `LimitedProduct.maximum`.

## Author

Fernando Tomas — MSIT Programming Course