def make_cart(customer_name):
    return {"customer": customer_name, "items": [], "total": 0.0}

def add_item(cart, item, price):
    cart["items"].append(item)
    cart["total"] = cart["total"] + price

def remove_item(cart, item, price):
    cart["items"].remove(item)
    cart["total"] = cart["total"] - price

def show_cart(cart):
    print(f"{cart['customer']}'s cart:")
    for item in cart["items"]:
        print(f"  - {item}")
    print(f"Total: ${cart['total']:.2f}")

cart = make_cart("Alice")
add_item(cart, "Wireless Mouse", 29.99)
add_item(cart, "Mechanical Keyboard", 89.99)
show_cart(cart)

cart = make_cart("Bob")
add_item(cart, "Bluetooth Headphones", 59.99)
add_item(cart, "USB Cable", 19.99)
show_cart(cart)