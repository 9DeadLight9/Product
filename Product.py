class Product:
    _product_count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product._product_count += 1

    
    def get_product_count():
        return Product._product_count

    def display_info(self):
        info = f"Product Name: {self.name}, Price: ${self.price:.2f}"
        info += f"\nTotal Products Created: {Product.get_product_count()}"
        return info

class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price)
        self.warranty_period = warranty_period

    def display_info(self):
        info = super().display_info()
        info += f", Warranty Period: {self.warranty_period} months"
        return info

class ClothingProduct(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def display_info(self):
        info = super().display_info()
        info += f", Size: {self.size}"
        return info


electronic_product = ElectronicProduct("Smartphone", 999.99, 24)
clothing_product = ClothingProduct("T-Shirt", 19.99, "M")

print(electronic_product.display_info())
print(clothing_product.display_info())
