"""
Singleton class for Singleton Pattern Example

This class demonstrates the classic Singleton pattern using eager initialization.
Only one instance of this class can exist throughout the application's lifetime.

Python offers several ways to implement Singleton:
1. Using __new__ method (shown here)
2. Using decorators
3. Using metaclasses
4. Using modules (Python modules are singletons by nature)
"""

import threading
from typing import Optional


class Singleton:
    """
    Classic Singleton implementation using eager initialization.
    
    This implementation ensures that only one instance of the class
    can be created, similar to the Java version with static initialization.
    """
    
    # Class variable to hold the single instance
    _instance: Optional['Singleton'] = None
    _lock = threading.Lock()  # Thread safety
    _initialized = False
    
    def __new__(cls) -> 'Singleton':
        """
        Override __new__ to control instance creation.
        
        This method is called before __init__ and controls object creation.
        It ensures only one instance is ever created.
        
        Returns:
            Singleton: The single instance of the class
        """
        if cls._instance is None:
            with cls._lock:  # Thread-safe double-checked locking
                if cls._instance is None:
                    print("인스턴스를 생성했습니다.")  # Korean: "Instance created"
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self) -> None:
        """
        Initialize the singleton instance.
        
        Note: This method can be called multiple times (each time getInstance
        is called), but it should only initialize once.
        """
        if not self._initialized:
            # Mark as initialized to prevent multiple initialization
            Singleton._initialized = True
    
    @classmethod
    def get_instance(cls) -> 'Singleton':
        """
        Class method to get the singleton instance.
        
        This method provides the same interface as the Java version.
        In Python, you can also just call Singleton() directly.
        
        Returns:
            Singleton: The single instance of the class
        """
        return cls()
    
    def some_business_method(self) -> str:
        """
        Example business method for the singleton.
        
        Returns:
            str: Some business logic result
        """
        return f"Singleton instance {id(self)} performing business logic"
    
    def __str__(self) -> str:
        """String representation of the singleton."""
        return f"Singleton instance (id: {id(self)})"
    
    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"Singleton(id={id(self)})"


class SingletonEager:
    """
    Alternative implementation using eager initialization (module-level).
    
    This approach creates the instance when the module is first imported,
    similar to the Java static initialization approach.
    """
    
    class _Singleton:
        """Inner class that contains the actual singleton logic."""
        
        def __init__(self):
            print("인스턴스를 생성했습니다. (Eager)")
        
        def some_business_method(self) -> str:
            return f"Eager Singleton instance {id(self)} performing business logic"
        
        def __str__(self) -> str:
            return f"EagerSingleton instance (id: {id(self)})"
    
    # Create the instance immediately (eager initialization)
    _instance = _Singleton()
    
    @classmethod
    def get_instance(cls):
        """Get the singleton instance."""
        return cls._instance


class SingletonMeta(type):
    """
    Metaclass-based Singleton implementation.
    
    This is a more advanced Python approach using metaclasses.
    The metaclass controls class creation itself.
    """
    
    _instances = {}
    _lock = threading.Lock()
    
    def __call__(cls, *args, **kwargs):
        """
        Control instance creation at the metaclass level.
        
        This method is called when someone tries to create an instance
        of a class that uses this metaclass.
        """
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    print(f"인스턴스를 생성했습니다. (Metaclass: {cls.__name__})")
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonWithMeta(metaclass=SingletonMeta):
    """
    Singleton implementation using metaclass.
    
    Any class that uses SingletonMeta as its metaclass will automatically
    become a singleton.
    """
    
    def __init__(self):
        """Initialize the singleton."""
        pass  # Initialization logic here
    
    def some_business_method(self) -> str:
        """Business method for metaclass singleton."""
        return f"Metaclass Singleton instance {id(self)} performing business logic"
    
    def __str__(self) -> str:
        """String representation."""
        return f"MetaclassSingleton instance (id: {id(self)})"


def singleton_decorator(cls):
    """
    Decorator-based Singleton implementation.
    
    This decorator can be applied to any class to make it a singleton.
    """
    instances = {}
    lock = threading.Lock()
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            with lock:
                if cls not in instances:
                    print(f"인스턴스를 생성했습니다. (Decorator: {cls.__name__})")
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance


@singleton_decorator
class SingletonWithDecorator:
    """
    Singleton implementation using decorator.
    
    The @singleton_decorator makes this class a singleton.
    """
    
    def __init__(self):
        """Initialize the decorated singleton."""
        pass
    
    def some_business_method(self) -> str:
        """Business method for decorated singleton."""
        return f"Decorator Singleton instance {id(self)} performing business logic"
    
    def __str__(self) -> str:
        """String representation."""
        return f"DecoratorSingleton instance (id: {id(self)})"
