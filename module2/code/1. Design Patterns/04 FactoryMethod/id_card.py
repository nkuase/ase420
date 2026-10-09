from product import Product

class IDCard(Product):
  def use(self):
    print(f"IDCard: using {self.name}.")
