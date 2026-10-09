from security_system import SecuritySystem
import time

def demonstrate_state_pattern():
    # Create our security system (context)
    system = SecuritySystem("Corporate Security System")
    
    # Define test scenarios with different times
    scenarios = [
        (10, "Morning - Business Hours"),
        (14, "Afternoon - Business Hours"),
        (18, "Evening - After Hours"),
        (22, "Night - After Hours"),
        (2, "Late Night - After Hours"),
        (8, "Early Morning - Before Hours"),
        (9, "Business Hours Resume")
    ]
    
    for hour, description in scenarios:
        print("\n" + "=" * 70)
        print(f"SCENARIO: {description} ({hour:02d}:00)")
        print("=" * 70)
        
        # Update time (may trigger state transition)
        system.set_time(hour)
        
        print(f"\nCurrent State: {system.get_current_state()}")
        print()
        
        system.use_safe()
        system.make_phone_call()
        system.trigger_alarm()

def main():
    demonstrate_state_pattern()

if __name__ == "__main__":
    main()
