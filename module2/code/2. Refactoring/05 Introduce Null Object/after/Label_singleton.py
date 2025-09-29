class Label:
    """Label class with nested singleton null object"""
    
    def __init__(self, label):
        self._label = label
    
    def display(self):
        print(f"display: {self._label}")
    
    def __str__(self):
        return f'"{self._label}"'
    
    def is_null(self):
        return False
    
    @staticmethod
    def new_null():
        """Factory method for null object"""
        return _NullLabel.get_instance()

class _NullLabel(Label):
    """Singleton null object for Label"""
    _instance = None
    
    def __init__(self):
        super().__init__("(none)")
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def display(self):
        pass
    
    def is_null(self):
        return True
