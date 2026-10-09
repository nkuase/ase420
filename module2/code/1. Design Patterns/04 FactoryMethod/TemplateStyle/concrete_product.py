from abstract_product import Product

# Concrete Products
class BasicProduct(Product):
    def use(self): print("Using Basic Product")

class PremiumProduct(Product):
    def use(self): print("Using Premium Product")