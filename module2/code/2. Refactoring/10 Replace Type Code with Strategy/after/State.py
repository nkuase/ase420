from abc import ABC, abstractmethod

class State(ABC):
    """Abstract base class for logger states"""
    
    @abstractmethod
    def get_type_code(self) -> int:
        """Get the type code for this state"""
        pass
