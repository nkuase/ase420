import sys
from safe_frame import SafeFrame
from PyQt6.QtWidgets import QApplication

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

if __name__ == "__main__":
    print("\nStarting GUI demonstration...")
    main()
