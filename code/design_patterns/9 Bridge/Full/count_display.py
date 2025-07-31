"""
Bridge Pattern - Refined Abstraction
This class extends the basic Display functionality with additional features.
It demonstrates how to extend the abstraction without affecting the implementation.
"""

from display import Display
from display_impl import DisplayImpl


class CountDisplay(Display):
    """
    Extended display class that can display content multiple times.
    This is a refined abstraction that adds new functionality
    to the basic Display class.
    """
    
    def __init__(self, impl: DisplayImpl):
        """
        Initialize with a concrete implementation.
        
        Args:
            impl (DisplayImpl): The implementation object to use
        """
        super().__init__(impl)
    
    def multi_display(self, times: int):
        """
        Display the content multiple times.
        This method adds new functionality to the basic display capability.
        
        Args:
            times (int): Number of times to display the content
        """
        self.open()
        for i in range(times):
            self.print()
        self.close()
