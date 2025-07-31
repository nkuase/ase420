"""
RandomNumberGenerator class for Observer Pattern Example

This concrete class extends NumberGenerator to provide random number generation.
It demonstrates how a concrete subject generates data and notifies observers.

This is a "Concrete Subject" in the Observer pattern.
"""

import random
import time
from number_generator import NumberGenerator


class RandomNumberGenerator(NumberGenerator):
    """
    Concrete implementation of NumberGenerator that generates random numbers.
    
    This class generates random numbers and notifies observers each time
    a new number is generated. It demonstrates the concrete subject in
    the Observer pattern.
    """
    
    def __init__(self, seed: int = None):
        """
        Initialize the random number generator.
        
        Args:
            seed (int, optional): Seed for the random number generator.
                                If None, uses system time.
        """
        super().__init__()
        self._random = random.Random(seed)
        self._number = 0
    
    def get_number(self) -> int:
        """
        Get the current number.
        
        Returns:
            int: The current random number
        """
        return self._number
    
    def execute(self) -> None:
        """
        Execute the random number generation process.
        
        Generates 20 random numbers between 0 and 49, notifying
        observers after each number is generated.
        """
        print("Starting random number generation...")
        
        for i in range(20):
            # Generate a new random number
            self._number = self._random.randint(0, 49)
            
            # Notify all observers about the change
            self.notify_observers()
            
            # Small delay to make the output visible
            time.sleep(0.1)
        
        print("Random number generation completed.")
    
    def execute_count(self, count: int) -> None:
        """
        Execute random number generation for a specific count.
        
        Args:
            count (int): Number of random numbers to generate
        """
        print(f"Starting random number generation ({count} numbers)...")
        
        for i in range(count):
            self._number = self._random.randint(0, 49)
            self.notify_observers()
            time.sleep(0.05)  # Shorter delay for custom count
        
        print(f"Generation completed ({count} numbers).")
    
    def execute_range(self, count: int, min_val: int, max_val: int) -> None:
        """
        Execute random number generation with custom range.
        
        Args:
            count (int): Number of random numbers to generate
            min_val (int): Minimum value (inclusive)
            max_val (int): Maximum value (inclusive)
        """
        print(f"Generating {count} numbers between {min_val} and {max_val}...")
        
        for i in range(count):
            self._number = self._random.randint(min_val, max_val)
            self.notify_observers()
            time.sleep(0.05)
        
        print("Range generation completed.")
    
    def set_seed(self, seed: int) -> None:
        """
        Set a new seed for the random number generator.
        
        Args:
            seed (int): New seed value
        """
        self._random = random.Random(seed)
    
    def get_current_seed_info(self) -> str:
        """
        Get information about the current random state.
        
        Returns:
            str: Information about the random generator state
        """
        return f"RandomNumberGenerator with current number: {self._number}"


class SequentialNumberGenerator(NumberGenerator):
    """
    Alternative concrete implementation that generates sequential numbers.
    
    This demonstrates how different concrete subjects can have different
    generation strategies while maintaining the same observer interface.
    """
    
    def __init__(self, start: int = 0, step: int = 1):
        """
        Initialize the sequential number generator.
        
        Args:
            start (int): Starting number
            step (int): Step size for each increment
        """
        super().__init__()
        self._current = start
        self._step = step
        self._start = start
    
    def get_number(self) -> int:
        """Get the current number."""
        return self._current
    
    def execute(self) -> None:
        """Execute sequential number generation."""
        print(f"Starting sequential generation (start={self._start}, step={self._step})...")
        
        for i in range(20):
            self.notify_observers()
            self._current += self._step
            time.sleep(0.1)
        
        print("Sequential generation completed.")
    
    def reset(self) -> None:
        """Reset to the starting number."""
        self._current = self._start
    
    def set_step(self, step: int) -> None:
        """Set a new step size."""
        self._step = step


class ManualNumberGenerator(NumberGenerator):
    """
    Manual number generator for testing and demonstration.
    
    This allows manual setting of numbers, useful for testing
    observer behavior with predictable values.
    """
    
    def __init__(self):
        """Initialize with number 0."""
        super().__init__()
        self._number = 0
    
    def get_number(self) -> int:
        """Get the current number."""
        return self._number
    
    def set_number(self, number: int) -> None:
        """
        Manually set a number and notify observers.
        
        Args:
            number (int): The number to set
        """
        self._number = number
        self.notify_observers()
    
    def execute(self) -> None:
        """Execute with predefined sequence."""
        predefined = [5, 15, 25, 35, 45, 10, 20, 30, 40, 0]
        
        print("Executing predefined sequence...")
        for num in predefined:
            self.set_number(num)
            time.sleep(0.2)
        
        print("Predefined sequence completed.")
