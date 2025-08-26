"""
Main module for Observer Pattern Example

This demonstrates the Observer pattern where an object (subject) maintains
a list of dependents (observers) and notifies them automatically when
its state changes. This is also known as the Publish-Subscribe pattern.

Key concepts demonstrated:
1. Subject/Observable (NumberGenerator) - maintains list of observers and notifies them
2. Observer interface - defines update contract for all observers
3. Concrete Observers - different ways of responding to notifications
4. Loose coupling between subject and observers
5. One-to-many dependency relationship

The number generation/display metaphor illustrates this pattern well:
- Number generator is the subject that changes
- Different displays (digit, graph, etc.) are observers
- Each observer can display the same data differently
- Observers can be added/removed dynamically
"""

from number_generator import NumberGenerator
from random_number_generator import RandomNumberGenerator, SequentialNumberGenerator, ManualNumberGenerator
from digit_observer import DigitObserver, FormattedDigitObserver
from graph_observer import GraphObserver, BarChartObserver, HistogramObserver
from observer import Observer
import time


def basic_observer_demo():
    """Demonstrate basic observer functionality (matching Java version)."""
    print("=== Basic Observer Demo ===")
    
    # Create the subject (number generator)
    generator: NumberGenerator = RandomNumberGenerator()
    
    # Create observers
    observer1: Observer = DigitObserver()
    observer2: Observer = GraphObserver()
    
    # Register observers with the subject
    generator.add_observer(observer1)
    generator.add_observer(observer2)
    
    print(f"Registered {generator.get_observer_count()} observers")
    print("Starting number generation...\n")
    
    # Execute - this will notify all observers
    generator.execute()
    
    print(f"\nDemo completed with {generator.get_observer_count()} observers")
    print()


def multiple_observer_types_demo():
    """Demonstrate multiple types of observers with the same subject."""
    print("=== Multiple Observer Types Demo ===")
    
    generator = RandomNumberGenerator(seed=42)  # Fixed seed for reproducible results
    
    # Create different types of observers
    digit_obs = DigitObserver("DigitDisplay")
    formatted_obs = FormattedDigitObserver("FormattedDisplay", "Value: ", " units")
    graph_obs = GraphObserver("StarGraph", "*", 30)
    bar_obs = BarChartObserver("BarChart", 25, show_scale=True)
    histogram_obs = HistogramObserver("Histogram", bin_size=10, display_frequency=8)
    
    # Register all observers
    observers = [digit_obs, formatted_obs, graph_obs, bar_obs, histogram_obs]
    for obs in observers:
        generator.add_observer(obs)
    
    print(f"Registered {len(observers)} different observer types:")
    for obs in observers:
        print(f"  - {obs}")
    
    print("\nGenerating 15 numbers...\n")
    generator.execute_count(15)
    
    # Show final statistics
    print("\n" + "="*50)
    print("Final Statistics:")
    print("="*50)
    formatted_obs.print_statistics()
    histogram_obs.display_final_histogram()
    
    print()


def dynamic_observer_management():
    """Demonstrate adding and removing observers dynamically."""
    print("=== Dynamic Observer Management ===")
    
    generator = ManualNumberGenerator()
    
    # Start with one observer
    digit_obs = DigitObserver("Primary")
    generator.add_observer(digit_obs)
    
    print("Starting with 1 observer:")
    generator.set_number(10)
    print(f"Observer count: {generator.get_observer_count()}")
    
    # Add more observers
    graph_obs = GraphObserver("Secondary", "#")
    bar_obs = BarChartObserver("Tertiary")
    
    generator.add_observer(graph_obs)
    generator.add_observer(bar_obs)
    
    print(f"\nAdded 2 more observers (total: {generator.get_observer_count()}):")
    generator.set_number(25)
    
    # Remove an observer
    generator.delete_observer(graph_obs)
    
    print(f"\nRemoved graph observer (total: {generator.get_observer_count()}):")
    generator.set_number(35)
    
    # Clear all observers
    generator.clear_observers()
    
    print(f"\nCleared all observers (total: {generator.get_observer_count()}):")
    generator.set_number(40)  # No output expected
    print("(No observer output - all removed)")
    
    print()


def different_subjects_demo():
    """Demonstrate different types of subjects with same observers."""
    print("=== Different Subjects Demo ===")
    
    # Create different types of number generators
    random_gen = RandomNumberGenerator(seed=123)
    sequential_gen = SequentialNumberGenerator(start=0, step=5)
    manual_gen = ManualNumberGenerator()
    
    # Create observers that will work with any generator
    digit_obs = DigitObserver("Universal")
    graph_obs = GraphObserver("Universal", "=", 20)
    
    generators = [
        ("Random Generator", random_gen),
        ("Sequential Generator", sequential_gen),
        ("Manual Generator", manual_gen)
    ]
    
    for name, generator in generators:
        print(f"\n{name}:")
        
        # Attach observers to current generator
        generator.add_observer(digit_obs)
        generator.add_observer(graph_obs)
        
        # Reset observer counters
        digit_obs.reset_count()
        graph_obs.reset_count()
        
        if isinstance(generator, ManualNumberGenerator):
            # Manual execution
            generator.execute()
        else:
            # Limited execution for demo
            generator.execute_count(5)
        
        print(f"  {digit_obs}")
        print(f"  {graph_obs}")
        
        # Clean up for next generator
        generator.clear_observers()
    
    print()


def observer_customization_demo():
    """Demonstrate observer customization and configuration."""
    print("=== Observer Customization Demo ===")
    
    generator = RandomNumberGenerator()
    
    # Create customized observers
    observers = [
        GraphObserver("Dots", ".", 50),
        GraphObserver("Hashes", "#", 30),
        GraphObserver("Stars", "*", 40),
        BarChartObserver("MinimalBar", width=20, show_scale=False, show_value=True),
        FormattedDigitObserver("Padded", "[", "]")
    ]
    
    for obs in observers:
        generator.add_observer(obs)
    
    print("Demonstrating customized observers:")
    generator.execute_count(8)
    
    # Demonstrate runtime customization
    print("\nChanging observer properties at runtime:")
    
    # Find and modify graph observers
    for obs in observers:
        if isinstance(obs, GraphObserver) and obs.get_name() == "Stars":
            obs.set_symbol("★")
            obs.set_scale_factor(0.5)
            break
    
    generator.execute_count(3)
    
    print()


def performance_and_scalability_demo():
    """Demonstrate performance characteristics with many observers."""
    print("=== Performance and Scalability Demo ===")
    
    generator = RandomNumberGenerator()
    
    # Create many observers
    num_observers = 20
    print(f"Creating {num_observers} observers...")
    
    for i in range(num_observers):
        if i % 3 == 0:
            obs = DigitObserver(f"Digit{i}")
        elif i % 3 == 1:
            obs = GraphObserver(f"Graph{i}", "*", 10)
        else:
            obs = FormattedDigitObserver(f"Format{i}", f"[{i}]:", "")
        
        generator.add_observer(obs)
    
    print(f"Registered {generator.get_observer_count()} observers")
    
    # Time the execution
    start_time = time.time()
    generator.execute_count(5)  # Small count to avoid too much output
    end_time = time.time()
    
    print(f"\nExecution with {num_observers} observers took {end_time - start_time:.3f} seconds")
    
    # Demonstrate that removing observers works
    print(f"\nRemoving half the observers...")
    observers_to_remove = list(generator._observers)[::2]  # Every other observer
    for obs in observers_to_remove:
        generator.delete_observer(obs)
    
    print(f"Now have {generator.get_observer_count()} observers")
    
    start_time = time.time()
    generator.execute_count(5)
    end_time = time.time()
    
    print(f"Execution with {generator.get_observer_count()} observers took {end_time - start_time:.3f} seconds")
    
    print()


def pattern_benefits_demo():
    """Demonstrate the benefits of the Observer pattern."""
    print("=== Observer Pattern Benefits ===")
    
    print("1. Loose Coupling:")
    print("   - Subject doesn't know concrete observer types")
    print("   - Observers don't know about each other")
    print("   - Easy to add new observer types")
    
    print("\n2. Dynamic Relationships:")
    print("   - Observers can be added/removed at runtime")
    print("   - No compile-time dependencies")
    
    print("\n3. Broadcast Communication:")
    print("   - One subject can notify many observers")
    print("   - All observers get notified simultaneously")
    
    print("\n4. Separation of Concerns:")
    print("   - Subject focuses on its core logic")
    print("   - Observers handle their specific display/logic")
    
    # Demonstrate with a practical example
    print("\n5. Practical Example - Stock Price Monitor:")
    
    class StockPrice(NumberGenerator):
        def __init__(self, symbol):
            super().__init__()
            self.symbol = symbol
            self.price = 100.0
        
        def get_number(self):
            return int(self.price)
        
        def set_price(self, price):
            self.price = price
            self.notify_observers()
        
        def execute(self):
            # Simulate price changes
            changes = [105, 98, 102, 110, 95, 108]
            for price in changes:
                self.set_price(price)
                time.sleep(0.2)
    
    # Create stock price subject
    stock = StockPrice("AAPL")
    
    # Different stakeholders (observers) interested in price changes
    retail_display = DigitObserver("RetailApp")
    trading_alert = FormattedDigitObserver("TradingAlert", "ALERT: AAPL = $", "")
    chart_display = GraphObserver("Chart", "█", 20)
    
    stock.add_observer(retail_display)
    stock.add_observer(trading_alert)
    stock.add_observer(chart_display)
    
    print("   Stock price updates with multiple stakeholders:")
    stock.execute()
    
    print()


def error_handling_demo():
    """Demonstrate error handling in the Observer pattern."""
    print("=== Error Handling Demo ===")
    
    generator = RandomNumberGenerator()
    
    class FaultyObserver(Observer):
        def __init__(self, name, fail_on_number=None):
            self.name = name
            self.fail_on_number = fail_on_number
        
        def update(self, generator):
            number = generator.get_number()
            if self.fail_on_number and number == self.fail_on_number:
                raise Exception(f"{self.name} failed on number {number}")
            print(f"{self.name}: {number} (OK)")
    
    # Add normal and faulty observers
    good_obs = DigitObserver("GoodObserver")
    faulty_obs = FaultyObserver("FaultyObserver", fail_on_number=25)
    another_good_obs = GraphObserver("AnotherGood", "*", 10)
    
    generator.add_observer(good_obs)
    generator.add_observer(faulty_obs)
    generator.add_observer(another_good_obs)
    
    # Enhanced notification with error handling
    class RobustNumberGenerator(RandomNumberGenerator):
        def notify_observers(self):
            """Enhanced notification with error handling."""
            failed_observers = []
            
            for observer in self._observers[:]:  # Copy list to avoid modification issues
                try:
                    observer.update(self)
                except Exception as e:
                    print(f"ERROR: Observer {observer} failed: {e}")
                    failed_observers.append(observer)
            
            # Optionally remove failed observers
            for failed_obs in failed_observers:
                print(f"Removing failed observer: {failed_obs}")
                self.delete_observer(failed_obs)
    
    robust_gen = RobustNumberGenerator()
    robust_gen.add_observer(good_obs)
    robust_gen.add_observer(faulty_obs)
    robust_gen.add_observer(another_good_obs)
    
    print("Testing error handling in observer notifications:")
    robust_gen.set_number(25)  # This should trigger the fault
    
    print(f"\nRemaining observers: {robust_gen.get_observer_count()}")
    robust_gen.set_number(30)  # Should work with remaining observers
    
    print()


def main():
    """Main function demonstrating the Observer pattern."""
    
    print("=== Observer Pattern Example ===\n")
    
    # Basic demonstration (matching Java version)
    basic_observer_demo()
    
    # Multiple observer types
    multiple_observer_types_demo()
    
    # Dynamic observer management
    dynamic_observer_management()
    
    # Different subjects
    different_subjects_demo()
    
    # Observer customization
    observer_customization_demo()
    
    # Performance and scalability
    performance_and_scalability_demo()
    
    # Pattern benefits
    pattern_benefits_demo()
    
    # Error handling
    error_handling_demo()
    
    print("="*60)
    print("Pattern Analysis:")
    print("="*60)
    
    print("\n1. Observer Pattern Structure:")
    print("   - Subject: Maintains list of observers and notifies them")
    print("   - Observer: Interface for objects that should be notified")
    print("   - ConcreteSubject: Stores state of interest to observers")
    print("   - ConcreteObserver: Implements update interface")
    
    print("\n2. Key Implementation Details:")
    print("   - Subject maintains list of observers")
    print("   - add_observer/delete_observer manage the list")
    print("   - notify_observers calls update on all observers")
    print("   - Observers receive reference to subject in update")
    
    print("\n3. Python-Specific Features:")
    print("   - List comprehensions for observer management")
    print("   - Exception handling in notification loops")
    print("   - Type hints for better interface definition")
    print("   - Property decorators for state access")
    
    print("\n4. Benefits Demonstrated:")
    print("   - Loose coupling between subject and observers")
    print("   - Dynamic relationship management")
    print("   - Broadcast communication pattern")
    print("   - Easy extension with new observer types")
    
    print("\n5. Real-World Applications:")
    print("   - Model-View-Controller (MVC) architectures")
    print("   - Event handling systems")
    print("   - Stock price monitoring")
    print("   - GUI component updates")
    print("   - Publish-subscribe messaging")
    
    print("\n6. Design Considerations:")
    print("   - Notification order may matter")
    print("   - Memory leaks if observers aren't removed")
    print("   - Performance with many observers")
    print("   - Error handling in observer updates")


if __name__ == "__main__":
    main()
