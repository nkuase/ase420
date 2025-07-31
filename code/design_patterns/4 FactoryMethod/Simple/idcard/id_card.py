from framework.product import Product


class IDCard(Product):
  
  def __init__(self, owner):
    print(f"Making {owner}'s card.")
    self._owner = owner
  
  def use(self):
    print(f"Using {self}.")
  
  def get_owner(self):
    return self._owner
  
  def __str__(self):
    return f"[IDCard:{self._owner}]"
  
  def __repr__(self):
    return f"IDCard('{self._owner}')"
  
  def __eq__(self, other):
    if not isinstance(other, IDCard):
      return False
    return self._owner == other._owner
  
  def __hash__(self):
    return hash(self._owner)
