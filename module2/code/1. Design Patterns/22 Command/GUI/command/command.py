from abc import ABC, abstractmethod

class Command(ABC):
    """
    Abstract Command interface for the Command design pattern.
    
    The Command pattern encapsulates a request as an object, thereby letting you
    parameterize clients with different requests, queue or log requests, and 
    support undoable operations.
    
    Key Benefits:
    - Decouples the object that invokes the operation from the one that performs it
    - Allows you to parameterize objects with operations
    - Allows you to queue operations, schedule their execution, or execute them remotely
    - Supports logging and undoing operations
    """
    
    @abstractmethod
    def execute(self):
        """
        Execute the command.
        
        This method should contain the logic to perform the encapsulated request.
        Concrete commands will implement this method to call the appropriate
        method(s) on their receiver object(s).
        """
        pass
    
    def __str__(self):
        """String representation of the command for debugging purposes"""
        return f"{self.__class__.__name__}()"
