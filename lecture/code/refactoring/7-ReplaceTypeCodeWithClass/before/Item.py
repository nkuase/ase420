class Item:
    """Item class using raw integer type codes (before refactoring)"""
    
    # Type code constants
    TYPECODE_BOOK = 0
    TYPECODE_DVD = 1
    TYPECODE_SOFTWARE = 2
    
    def __init__(self, typecode: int, title: str, price: int):
        self.typecode = typecode
        self.title = title
        self.price = price
        
    def get_typecode(self) -> int:
        return self.typecode
        
    def get_title(self) -> str:
        return self.title
        
    def get_price(self) -> int:
        return self.price
        
    def __str__(self):
        return f"[ {self.get_typecode()}, {self.get_title()}, {self.get_price()} ]"
