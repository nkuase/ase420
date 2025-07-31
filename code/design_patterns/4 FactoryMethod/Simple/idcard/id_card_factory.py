from framework.factory import Factory
from .id_card import IDCard


class IDCardFactory(Factory):
  
  def __init__(self):
    self._created_cards = []
  
  def create_product(self, owner):
    return IDCard(owner)
  
  def register_product(self, product):
    print(f"{product} is registered")
    
    if isinstance(product, IDCard):
      self._created_cards.append(product)
  
  def get_created_cards(self):
    return self._created_cards.copy()
  
  def get_card_count(self):
    return len(self._created_cards)
  
  def find_card_by_owner(self, owner):
    for card in self._created_cards:
      if card.get_owner() == owner:
        return card
    raise ValueError(f"No card found for owner: {owner}")
  
  def __str__(self):
    return f"IDCardFactory (created {len(self._created_cards)} cards)"
  
  def __repr__(self):
    return f"IDCardFactory(created_cards={len(self._created_cards)})"
