from product import Product

class SuperCard(Product):
  def use(self):
    print(f"Supercard: using {self.name}.")
