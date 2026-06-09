'''
Give Each Cart Its Own State
Build a `Cart` class where each instance stores its own customer name, item list, and running total. The cart for `"Alice"` receives `"Pen"` for `2.50` and `"Mug"` for `13.00`; the cart for `"Bob"` receives `"Tea"` for `7.25`.

The `summary` method should report the customer name, item count, and total formatted to 2 decimal places. The `item_names` method should return the cart's item names joined with `", "`.
'''

class Cart:
    def __init__(self, customer):
        self.customer = customer
        self.items = []
        self.total = 0.0

    def add_item(self, item, price):
        self.items.append(item)
        self.total += price

    def summary(self):
        return f"{self.customer}: {len(self.items)} items, total ${self.total:.2f}"

    def item_names(self):
        return ", ".join(self.items)


alice_cart = Cart("Alice")
alice_cart.add_item("Pen", 2.50)
alice_cart.add_item("Mug", 13.00)

bob_cart = Cart("Bob")
bob_cart.add_item("Tea", 7.25)

print(alice_cart.summary())
print(bob_cart.summary())
print(f"Alice items: {alice_cart.item_names()}")
print(f"Bob items: {bob_cart.item_names()}")


'''
Expected Output:
Alice: 2 items, total $15.50
Bob: 1 items, total $7.25
Alice items: Pen, Mug
Bob items: Tea
'''