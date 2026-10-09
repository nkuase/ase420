from ItemType import ItemType

class Item:
    """Item class using type-safe ItemType (after refactoring)"""
    
    def __init__(self, itemtype: ItemType, title: str, price: int):
        self.itemtype = itemtype
        self.title = title
        self.price = price
        
    def get_typecode(self):
        return self.itemtype.get_typecode()
        
    def get_title(self) -> str:
        return self.title
        
    def get_price(self) -> int:
        return self.price
        
    def __str__(self):
        return f"[ {self.itemtype.get_typecode()}, {self.get_title()}, {self.get_price()} ]"
