"""
GraphObserver class for Observer Pattern Example

This concrete observer displays numbers as visual graphs using asterisks.
It demonstrates how observers can present the same data in different visual formats.

This is a "Concrete Observer" in the Observer pattern.
"""

import time
from observer import Observer
from number_generator import NumberGenerator


class GraphObserver(Observer):
    """
    Concrete observer that displays numbers as visual graphs.
    
    This observer converts numeric values into visual representations
    using asterisk characters, where each unit is represented by one asterisk.
    """
    
    def __init__(self, name: str = "GraphObserver", 
                 symbol: str = "*", 
                 max_width: int = 50):
        """
        Initialize the graph observer.
        
        Args:
            name (str): Name identifier for this observer
            symbol (str): Character to use for the graph (default: "*")
            max_width (int): Maximum width of the graph display
        """
        self._name = name
        self._symbol = symbol
        self._max_width = max_width
        self._update_count = 0
        self._scale_factor = 1.0
    
    def update(self, generator: NumberGenerator) -> None:
        """
        Update method that displays the number as a visual graph.
        
        Args:
            generator (NumberGenerator): The subject that changed
        """
        self._update_count += 1
        current_number = generator.get_number()
        
        # Calculate the number of symbols to display
        symbol_count = int(current_number * self._scale_factor)
        
        # Ensure we don't exceed max width
        if symbol_count > self._max_width:
            symbol_count = self._max_width
            overflow_indicator = f" (>{self._max_width})"
        else:
            overflow_indicator = ""
        
        # Create the graph
        graph = self._symbol * symbol_count
        
        print(f"{self._name}: {graph}{overflow_indicator}")
        
        # Small delay to simulate processing time
        try:
            time.sleep(0.1)
        except KeyboardInterrupt:
            pass
    
    def set_scale_factor(self, factor: float) -> None:
        """
        Set the scale factor for the graph display.
        
        Args:
            factor (float): Scale factor (1.0 = normal, 0.5 = half size, 2.0 = double size)
        """
        if factor <= 0:
            raise ValueError("Scale factor must be positive")
        self._scale_factor = factor
    
    def set_symbol(self, symbol: str) -> None:
        """
        Change the symbol used for the graph.
        
        Args:
            symbol (str): New symbol to use
        """
        if len(symbol) != 1:
            raise ValueError("Symbol must be exactly one character")
        self._symbol = symbol
    
    def set_max_width(self, max_width: int) -> None:
        """
        Set the maximum width for the graph display.
        
        Args:
            max_width (int): Maximum number of symbols to display
        """
        if max_width <= 0:
            raise ValueError("Max width must be positive")
        self._max_width = max_width
    
    def get_name(self) -> str:
        """Get the name of this observer."""
        return self._name
    
    def get_update_count(self) -> int:
        """Get the number of updates received."""
        return self._update_count
    
    def reset_count(self) -> None:
        """Reset the update counter."""
        self._update_count = 0
    
    def __str__(self) -> str:
        """String representation of the observer."""
        return f"{self._name} (symbol='{self._symbol}', updates={self._update_count})"
    
    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return (f"GraphObserver('{self._name}', symbol='{self._symbol}', "
                f"max_width={self._max_width}, scale={self._scale_factor})")


class BarChartObserver(Observer):
    """
    Enhanced graph observer that displays numbers as horizontal bar charts.
    
    This demonstrates a more sophisticated visual representation with
    labels, scales, and better formatting.
    """
    
    def __init__(self, name: str = "BarChart", 
                 width: int = 40, 
                 show_scale: bool = True,
                 show_value: bool = True):
        """
        Initialize the bar chart observer.
        
        Args:
            name (str): Name identifier for this observer
            width (int): Width of the bar chart
            show_scale (bool): Whether to show scale markers
            show_value (bool): Whether to show numeric value
        """
        self._name = name
        self._width = width
        self._show_scale = show_scale
        self._show_value = show_value
        self._update_count = 0
        self._max_observed = 0
    
    def update(self, generator: NumberGenerator) -> None:
        """
        Update method that displays a formatted bar chart.
        
        Args:
            generator (NumberGenerator): The subject that changed
        """
        self._update_count += 1
        current_number = generator.get_number()
        
        # Track maximum value for scaling
        if current_number > self._max_observed:
            self._max_observed = current_number
        
        # Calculate bar length (scale to max observed value)
        if self._max_observed > 0:
            bar_length = int((current_number / max(self._max_observed, 50)) * self._width)
        else:
            bar_length = 0
        
        # Create the bar
        bar = "█" * bar_length
        empty = "░" * (self._width - bar_length)
        
        # Format the display
        display = f"{self._name}: |{bar}{empty}|"
        
        if self._show_value:
            display += f" {current_number:2d}"
        
        if self._show_scale and self._update_count % 5 == 1:
            # Show scale every 5th update
            scale_line = f"{' ' * (len(self._name) + 2)}|{'-' * self._width}|"
            scale_nums = f"{' ' * (len(self._name) + 2)} 0{' ' * (self._width - 10)}50"
            print(scale_line)
            print(scale_nums)
        
        print(display)
        
        try:
            time.sleep(0.1)
        except KeyboardInterrupt:
            pass
    
    def get_max_observed(self) -> int:
        """Get the maximum value observed so far."""
        return self._max_observed
    
    def reset_max(self) -> None:
        """Reset the maximum observed value."""
        self._max_observed = 0
    
    def __str__(self) -> str:
        """String representation of the observer."""
        return f"{self._name} (width={self._width}, max_observed={self._max_observed})"


class HistogramObserver(Observer):
    """
    Observer that maintains a histogram of observed values.
    
    This demonstrates how observers can accumulate and analyze data
    over time rather than just displaying current values.
    """
    
    def __init__(self, name: str = "Histogram", 
                 bin_size: int = 10, 
                 display_frequency: int = 10):
        """
        Initialize the histogram observer.
        
        Args:
            name (str): Name identifier for this observer
            bin_size (int): Size of each histogram bin
            display_frequency (int): How often to display the histogram
        """
        self._name = name
        self._bin_size = bin_size
        self._display_frequency = display_frequency
        self._update_count = 0
        self._histogram = {}  # bin -> count
    
    def update(self, generator: NumberGenerator) -> None:
        """
        Update the histogram with the new value.
        
        Args:
            generator (NumberGenerator): The subject that changed
        """
        self._update_count += 1
        current_number = generator.get_number()
        
        # Determine which bin this value belongs to
        bin_key = (current_number // self._bin_size) * self._bin_size
        
        # Update histogram
        if bin_key not in self._histogram:
            self._histogram[bin_key] = 0
        self._histogram[bin_key] += 1
        
        # Display histogram periodically
        if self._update_count % self._display_frequency == 0:
            self._display_histogram()
    
    def _display_histogram(self) -> None:
        """Display the current histogram."""
        print(f"\n{self._name} (after {self._update_count} values):")
        
        if not self._histogram:
            print("  No data")
            return
        
        # Sort bins for display
        sorted_bins = sorted(self._histogram.keys())
        max_count = max(self._histogram.values())
        
        for bin_start in sorted_bins:
            bin_end = bin_start + self._bin_size - 1
            count = self._histogram[bin_start]
            
            # Create visual bar
            bar_length = int((count / max_count) * 20) if max_count > 0 else 0
            bar = "▪" * bar_length
            
            print(f"  {bin_start:2d}-{bin_end:2d}: {bar} ({count})")
        print()
    
    def get_histogram(self) -> dict:
        """Get a copy of the current histogram."""
        return self._histogram.copy()
    
    def display_final_histogram(self) -> None:
        """Display the final histogram."""
        print(f"\nFinal {self._name}:")
        self._display_histogram()
    
    def reset_histogram(self) -> None:
        """Reset the histogram data."""
        self._histogram.clear()
        self._update_count = 0
