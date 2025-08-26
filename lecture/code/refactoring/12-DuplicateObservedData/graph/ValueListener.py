from abc import abstractmethod

class ValueListener:
    """Interface for value change listeners"""
    
    @abstractmethod
    def value_changed(self, event):
        pass
