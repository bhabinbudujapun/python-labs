'''
Create a Product Class
Define a `Product` class that bundles three pieces of state: the string name `"Notebook"`, the float price `4.5`, and the integer stock count `12`.
The `__init__` method should store those values on `self.name`, `self.price`, and `self.stock`. The `label` method should return one formatted string using the stored attributes, with the price displayed to exactly 2 decimal places.
'''

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def label(self):
        # Expected Output-> Notebook: $4.50 (12 in stock)
        return f"{self.name}: ${self.price:.2f} ({self.stock} in stock)"
    
product = Product("Notebook", 4.5, 12)
print(type(product))
print(product.label())