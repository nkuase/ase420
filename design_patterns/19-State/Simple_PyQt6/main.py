import sys
from PyQt6.QtWidgets import QApplication
from safe_frame import SafeFrame

def main():
    """
    Main function demonstrating the State Design Pattern using PyQt6.
    
    This example shows a security system that behaves differently based on
    the current state (daytime vs nighttime). The same user actions produce
    different behaviors depending on the time of day.
    
    Educational Value:
    - Demonstrates the State pattern in a real-world scenario
    - Shows how state transitions can be automatic (time-based)
    - Illustrates how the same interface can have different implementations
    - Combines State pattern with Singleton pattern for state management
    """
    
    print("=== State Pattern Demo with PyQt6 ===\n")
    
    print("Creating Security System with State Pattern...")
    print("\nSystem Behavior:")
    print("📅 DAYTIME (9:00-17:00):")
    print("  - Safe usage: Normal operation (logged)")
    print("  - Emergency alarm: Calls security center")  
    print("  - Phone calls: Normal calls to security")
    
    print("\n🌙 NIGHTTIME (17:00-9:00):")
    print("  - Safe usage: EMERGENCY ALERT! (unauthorized access)")
    print("  - Emergency alarm: Calls security center")
    print("  - Phone calls: Recorded for security review")
    
    print(f"\n{'='*60}")
    print("State Pattern Key Concepts Demonstrated:")
    print("1. State Interface: All states implement the same methods")
    print("2. Concrete States: DayState and NightState with different behaviors")
    print("3. Context: SafeFrame maintains current state and delegates actions")
    print("4. State Transitions: Automatic transitions based on time")
    print("5. Polymorphism: Same method calls, different behaviors")
    print(f"{'='*60}")
    
    print(f"\n{'='*60}")
    print("How to use the demo:")
    print("1. Watch the clock automatically cycle through 24 hours")
    print("2. Notice state transitions at 9:00 (to Day) and 17:00 (to Night)")
    print("3. Try clicking buttons during different times of day")
    print("4. Observe how the same actions produce different behaviors")
    print("5. Close the window to exit")
    print(f"{'='*60}")
    
    try:
        # Create PyQt6 application
        app = QApplication(sys.argv)
        
        # Create main window
        safe_frame = SafeFrame("State Pattern Demo - Security System (PyQt6)")
        safe_frame.show()
        
        # Start the application event loop
        sys.exit(app.exec())
        
    except KeyboardInterrupt:
        print("\nDemo interrupted by user")
    except Exception as e:
        print(f"Error running demo: {e}")
        print("Note: This demo requires PyQt6 to be installed")
        print("Install with: pip install PyQt6")

def explain_state_pattern():
    """
    Educational explanation of the State Design Pattern.
    """
    print("\n" + "="*70)
    print("STATE DESIGN PATTERN EXPLANATION")
    print("="*70)
    
    print("\n🎯 INTENT:")
    print("Allow an object to alter its behavior when its internal state changes.")
    print("The object will appear to change its class.")
    
    print("\n🏗️ STRUCTURE:")
    print("1. State (Interface): Defines interface for encapsulating behavior")
    print("2. Concrete States: Implement behavior associated with a state")
    print("3. Context: Maintains current state and delegates state-specific requests")
    
    print("\n✅ BENEFITS:")
    print("• Eliminates large conditional statements")
    print("• Makes state transitions explicit")
    print("• State-specific behavior is localized")
    print("• Easy to add new states")
    print("• Promotes loose coupling")
    
    print("\n🎓 REAL-WORLD APPLICATIONS:")
    print("• TCP connection states (LISTEN, ESTABLISHED, CLOSED)")
    print("• Game character states (IDLE, RUNNING, JUMPING)")
    print("• Order processing (PENDING, CONFIRMED, SHIPPED)")
    print("• Media player states (PLAYING, PAUSED, STOPPED)")
    print("• Authentication states (LOGGED_IN, LOGGED_OUT)")
    
    print("\n💡 KEY INSIGHT:")
    print("Instead of having complex if-else chains, each state becomes")
    print("a separate class with its own implementation of the same interface.")
    print("This makes the code more maintainable and extensible.")

if __name__ == "__main__":
    explain_state_pattern()
    print("\nStarting GUI demonstration...")
    main()
