"""
DigitObserver class for Observer Pattern Example

This concrete observer displays numbers in digit format when notified.
It demonstrates how different observers can react differently to the same event.

This is a "Concrete Observer" in the Observer pattern.
"""

import time
from observer import Observer
from number_generator import NumberGenerator


class DigitObserver(Observer):
    """
    Concrete observer that displays numbers in digit format.
    
    This observer simply prints the current number when notified.
    It represents a simple, direct way of displaying the data.
    """
    
    def __init__(self, name: str = "DigitObserver"):
        """
        Initialize the digit observer.
        
        Args:
            name (str): Name identifier for this observer
        """
        self._name = name
        self._update_count = 0
    
    def update(self, generator: NumberGenerator) -> None:
        """
        Update method called when the observed subject changes.
        
        Displays the current number in a simple digit format.
        
        Args:
            generator (NumberGenerator): The subject that changed
        """
        self._update_count += 1
        current_number = generator.get_number()
        
        print(f"{self._name}: {current_number}")
        
        # Small delay to simulate processing time
        try:
            time.sleep(0.1)
        except KeyboardInterrupt:
            pass  # Allow graceful interruption
    
    def get_name(self) -> str:
        """
        Get the name of this observer.
        
        Returns:
            str: The observer's name
        """
        return self._name
    
    def get_update_count(self) -> int:
        """
        Get the number of times this observer has been updated.
        
        Returns:
            int: The update count
        """
        return self._update_count
    
    def reset_count(self) -> None:
        """Reset the update counter."""
        self._update_count = 0
    
    def __str__(self) -> str:
        """String representation of the observer."""
        return f"{self._name} (updates: {self._update_count})"
    
    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"DigitObserver('{self._name}', updates={self._update_count})"


class FormattedDigitObserver(Observer):
    """
    Enhanced digit observer with formatting options.
    
    This demonstrates how observers can have different behaviors
    while implementing the same interface.
    """
    
    def __init__(self, name: str = "FormattedDigit", 
                 prefix: str = "Number: ", 
                 suffix: str = ""):
        """
        Initialize the formatted digit observer.
        
        Args:
            name (str): Name identifier for this observer
            prefix (str): Text to display before the number
            suffix (str): Text to display after the number
        """
        self._name = name
        self._prefix = prefix
        self._suffix = suffix
        self._update_count = 0
        self._min_value = None
        self._max_value = None
        self._sum = 0
    
    def update(self, generator: NumberGenerator) -> None:
        """
        Update with formatted display and statistics tracking.
        
        Args:
            generator (NumberGenerator): The subject that changed
        """
        self._update_count += 1
        current_number = generator.get_number()
        
        # Update statistics
        self._sum += current_number
        if self._min_value is None or current_number < self._min_value:
            self._min_value = current_number
        if self._max_value is None or current_number > self._max_value:
            self._max_value = current_number
        
        # Display formatted number
        print(f"{self._name}: {self._prefix}{current_number:02d}{self._suffix}")
        
        try:
            time.sleep(0.1)
        except KeyboardInterrupt:
            pass
    
    def get_statistics(self) -> dict:
        """
        Get statistics about observed numbers.
        
        Returns:
            dict: Statistics including min, max, average, count
        """
        if self._update_count == 0:
            return {"count": 0, "min": None, "max": None, "average": None, "sum": 0}
        
        return {
            "count": self._update_count,
            "min": self._min_value,
            "max": self._max_value,
            "average": self._sum / self._update_count,
            "sum": self._sum
        }
    
    def print_statistics(self) -> None:
        """Print statistics about observed numbers."""
        stats = self.get_statistics()
        
        if stats["count"] == 0:
            print(f"{self._name} statistics: No updates received")
            return
        
        print(f"{self._name} statistics:")
        print(f"  Count: {stats['count']}")
        print(f"  Min: {stats['min']}")
        print(f"  Max: {stats['max']}")
        print(f"  Average: {stats['average']:.2f}")
        print(f"  Sum: {stats['sum']}")
    
    def reset_statistics(self) -> None:
        """Reset all statistics."""
        self._update_count = 0
        self._min_value = None
        self._max_value = None
        self._sum = 0
    
    def __str__(self) -> str:
        """String representation with statistics."""
        stats = self.get_statistics()
        if stats["count"] == 0:
            return f"{self._name} (no updates)"
        return f"{self._name} (updates: {stats['count']}, avg: {stats['average']:.1f})"
