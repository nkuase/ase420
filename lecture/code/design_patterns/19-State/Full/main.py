"""
State Pattern Demo
This example demonstrates the State pattern through a security system
that behaves differently during day and night hours.

Key concepts demonstrated:
1. State-dependent behavior without complex conditional statements
2. Clean state transitions based on external events (time changes)
3. Encapsulation of state-specific behavior in separate classes
4. Polymorphic delegation to state objects
"""

import threading
import time
from safe_frame import SafeFrame


def time_simulator(safe_frame):
    """
    Simulate the passage of time by cycling through 24 hours.
    
    Args:
        safe_frame (SafeFrame): The security system to update
    """
    hour = 0
    while True:
        try:
            safe_frame.set_clock(hour)
            hour = (hour + 1) % 24
            time.sleep(2)  # Update every 2 seconds for demo
        except:
            # Window was closed
            break


def main():
    """
    Main function that demonstrates the State pattern.
    Creates a security system GUI that changes behavior based on time of day.
    """
    print("=== State Pattern Demo ===\n")
    
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
    print("How to use the demo:")
    print("1. Watch the clock automatically cycle through 24 hours")
    print("2. Notice state transitions at 9:00 (to Day) and 17:00 (to Night)")
    print("3. Try clicking buttons during different times of day")
    print("4. Observe how the same actions produce different behaviors")
    print("5. Close the window to exit")
    print(f"{'='*60}")
    
    try:
        # Create the security system window
        safe_frame = SafeFrame("State Pattern Demo - Security System")
        
        # Start time simulation in a separate thread
        time_thread = threading.Thread(target=time_simulator, args=(safe_frame,), daemon=True)
        time_thread.start()
        
        # Start the GUI event loop
        safe_frame.mainloop()
        
    except KeyboardInterrupt:
        print("\nDemo interrupted by user")
    except Exception as e:
        print(f"Error running demo: {e}")
        print("Note: This demo requires a GUI environment with tkinter support")
    
    print("\nState Pattern Benefits Demonstrated:")
    print("✅ Clean State Management: No complex if-else chains for state logic")
    print("✅ Easy Extension: New states can be added without modifying existing code")
    print("✅ Encapsulation: Each state encapsulates its own behavior")
    print("✅ Polymorphism: Same interface, different implementations per state")
    print("✅ Maintainability: State-specific code is isolated and easy to modify")
    
    print("\nKey Points:")
    print("- State pattern eliminates complex conditional statements")
    print("- Each state is responsible for its own behavior and transitions")
    print("- Context delegates behavior to the current state object")
    print("- States can be implemented as singletons to save memory")
    print("- Useful when object behavior depends significantly on its state")
    print("- Makes state transitions explicit and easier to understand")


if __name__ == "__main__":
    main()
