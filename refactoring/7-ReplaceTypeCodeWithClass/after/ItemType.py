class ItemType:
    """Type-safe item type class"""
    
    def __init__(self, typecode: int):
        self._typecode = typecode
        
    def get_typecode(self) -> int:
        return self._typecode

# Type-safe constants        
ItemType.BOOK = ItemType(0)
ItemType.DVD = ItemType(1)
ItemType.SOFTWARE = ItemType(2)
