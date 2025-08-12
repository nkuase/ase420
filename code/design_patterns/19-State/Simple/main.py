import threading
import time
from safe_frame import SafeFrame

def time_simulator(safe_frame):
  hour = 0
  while True:
    try:
      safe_frame.set_clock(hour)
      hour = (hour + 1) % 24
      time.sleep(2)
    except:
      break

def main():
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
    safe_frame = SafeFrame("State Pattern Demo - Security System")
    
    time_thread = threading.Thread(target=time_simulator, args=(safe_frame,), daemon=True)
    time_thread.start()
    
    safe_frame.mainloop()
    
  except KeyboardInterrupt:
    print("\nDemo interrupted by user")
  except Exception as e:
    print(f"Error running demo: {e}")
    print("Note: This demo requires a GUI environment with tkinter support")


if __name__ == "__main__":
  main()
