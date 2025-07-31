"""
Main module for Singleton Pattern Example

This demonstrates various approaches to implementing the Singleton pattern in Python.
The Singleton pattern ensures that only one instance of a class exists and provides
a global access point to that instance.

Python offers several unique ways to implement Singleton that don't exist in Java:
1. __new__ method control
2. Decorators
3. Metaclasses
4. Module-level instances

Key concepts demonstrated:
1. Instance uniqueness - only one instance exists
2. Global access - same instance accessible everywhere
3. Thread safety - safe in multi-threaded environments
4. Different implementation approaches
"""

import threading
import time
from singleton import (
    Singleton, 
    SingletonEager, 
    SingletonWithMeta, 
    SingletonWithDecorator
)


def test_basic_singleton():
    """Test the basic Singleton implementation."""
    print("=== Testing Basic Singleton ===")
    
    print("Start.")
    
    # Get instances using different methods
    obj1 = Singleton.get_instance()
    obj2 = Singleton.get_instance()
    
    # Also test direct instantiation
    obj3 = Singleton()
    
    # Check if they're the same instance
    if obj1 is obj2 is obj3:
        print("obj1, obj2, obj3는 같은 인스턴스입니다.")
    else:
        print("obj1, obj2, obj3는 같은 인스턴스가 아닙니다.")
    
    print(f"obj1 id: {id(obj1)}")
    print(f"obj2 id: {id(obj2)}")
    print(f"obj3 id: {id(obj3)}")
    
    # Test business functionality
    print(f"Business method: {obj1.some_business_method()}")
    
    print("End.\n")


def test_eager_singleton():
    """Test the eager initialization Singleton."""
    print("=== Testing Eager Singleton ===")
    
    obj1 = SingletonEager.get_instance()
    obj2 = SingletonEager.get_instance()
    
    if obj1 is obj2:
        print("Eager singleton instances are the same")
    
    print(f"Eager singleton: {obj1}")
    print(f"Business method: {obj1.some_business_method()}")
    print()


def test_metaclass_singleton():
    """Test the metaclass-based Singleton."""
    print("=== Testing Metaclass Singleton ===")
    
    obj1 = SingletonWithMeta()
    obj2 = SingletonWithMeta()
    
    if obj1 is obj2:
        print("Metaclass singleton instances are the same")
    
    print(f"Metaclass singleton: {obj1}")
    print(f"Business method: {obj1.some_business_method()}")
    print()


def test_decorator_singleton():
    """Test the decorator-based Singleton."""
    print("=== Testing Decorator Singleton ===")
    
    obj1 = SingletonWithDecorator()
    obj2 = SingletonWithDecorator()
    
    if obj1 is obj2:
        print("Decorator singleton instances are the same")
    
    print(f"Decorator singleton: {obj1}")
    print(f"Business method: {obj1.some_business_method()}")
    print()


def test_thread_safety():
    """Test thread safety of the Singleton implementation."""
    print("=== Testing Thread Safety ===")
    
    instances = []
    
    def create_singleton():
        """Function to create singleton in a thread."""
        instance = Singleton.get_instance()
        instances.append(instance)
    
    # Create multiple threads
    threads = []
    for i in range(10):
        thread = threading.Thread(target=create_singleton)
        threads.append(thread)
    
    # Start all threads
    print("Starting 10 threads to create singleton instances...")
    for thread in threads:
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    # Check if all instances are the same
    first_instance = instances[0]
    all_same = all(instance is first_instance for instance in instances)
    
    if all_same:
        print(f"✓ Thread safety test passed: All {len(instances)} instances are the same")
        print(f"  Instance ID: {id(first_instance)}")
    else:
        print("✗ Thread safety test failed: Different instances found")
        unique_instances = set(id(instance) for instance in instances)
        print(f"  Found {len(unique_instances)} unique instances")
    
    print()


def compare_singleton_approaches():
    """Compare different Singleton implementation approaches."""
    print("=== Comparing Singleton Approaches ===")
    
    # Test each approach
    basic = Singleton()
    eager = SingletonEager.get_instance()
    meta = SingletonWithMeta()
    deco = SingletonWithDecorator()
    
    print("Approach Comparison:")
    print(f"1. Basic (__new__):  {basic}")
    print(f"2. Eager (module):   {eager}")
    print(f"3. Metaclass:        {meta}")
    print(f"4. Decorator:        {deco}")
    
    # Test that each maintains its own singleton property
    basic2 = Singleton()
    eager2 = SingletonEager.get_instance()
    meta2 = SingletonWithMeta()
    deco2 = SingletonWithDecorator()
    
    print("\nSingleton Property Check:")
    print(f"1. Basic:     {basic is basic2}")
    print(f"2. Eager:     {eager is eager2}")
    print(f"3. Metaclass: {meta is meta2}")
    print(f"4. Decorator: {deco is deco2}")
    print()


def demonstrate_singleton_benefits():
    """Demonstrate the benefits of using Singleton pattern."""
    print("=== Singleton Pattern Benefits ===")
    
    # Global access point
    print("1. Global Access Point:")
    print("   - Same instance accessible from anywhere")
    
    instance1 = Singleton()
    instance2 = Singleton.get_instance()
    
    print(f"   From different access methods: {instance1 is instance2}")
    
    # Resource management
    print("\n2. Resource Management:")
    print("   - Only one instance reduces memory usage")
    print(f"   - Single instance ID: {id(instance1)}")
    
    # Consistency
    print("\n3. State Consistency:")
    print("   - All references share the same state")
    
    # Control over instantiation
    print("\n4. Controlled Instantiation:")
    print("   - Prevents accidental multiple instances")
    print("   - Ensures proper initialization")
    
    print()


def show_antipatterns_and_alternatives():
    """Show common anti-patterns and when NOT to use Singleton."""
    print("=== When NOT to Use Singleton ===")
    
    print("1. Anti-patterns:")
    print("   - Using Singleton just for global access")
    print("   - Making everything a Singleton")
    print("   - Using Singleton for stateless objects")
    
    print("\n2. Problems with Singleton:")
    print("   - Makes unit testing difficult")
    print("   - Creates tight coupling")
    print("   - Violates Single Responsibility Principle")
    
    print("\n3. Alternatives to consider:")
    print("   - Dependency Injection")
    print("   - Factory Pattern")
    print("   - Module-level functions (in Python)")
    print("   - Configuration objects")
    
    print("\n4. Python-specific note:")
    print("   - Modules are natural singletons in Python")
    print("   - Consider using module-level variables instead")
    
    print()


def main():
    """Main function demonstrating various Singleton implementations."""
    
    print("=== Singleton Pattern Examples in Python ===\n")
    
    # Test basic singleton (similar to Java version)
    test_basic_singleton()
    
    # Test different Python approaches
    test_eager_singleton()
    test_metaclass_singleton()
    test_decorator_singleton()
    
    # Test thread safety
    test_thread_safety()
    
    # Compare approaches
    compare_singleton_approaches()
    
    # Demonstrate benefits
    demonstrate_singleton_benefits()
    
    # Show when not to use
    show_antipatterns_and_alternatives()
    
    print("="*60)
    print("Pattern Analysis Summary:")
    print("="*60)
    
    print("\n1. Singleton Pattern Purpose:")
    print("   - Ensure only one instance of a class")
    print("   - Provide global access to that instance")
    print("   - Control object creation")
    
    print("\n2. Python Implementation Options:")
    print("   - __new__ method override (most common)")
    print("   - Metaclass (advanced)")
    print("   - Decorator (functional approach)")
    print("   - Module-level (Pythonic)")
    
    print("\n3. Key Considerations:")
    print("   - Thread safety in multi-threaded applications")
    print("   - Testing implications")
    print("   - Design complexity vs. benefits")
    
    print("\n4. Best Practices:")
    print("   - Use sparingly and only when truly needed")
    print("   - Consider alternatives like dependency injection")
    print("   - In Python, often a module is sufficient")
    
    print("\n5. Real-world Use Cases:")
    print("   - Database connection pools")
    print("   - Logger instances")
    print("   - Configuration managers")
    print("   - Cache managers")


if __name__ == "__main__":
    main()
