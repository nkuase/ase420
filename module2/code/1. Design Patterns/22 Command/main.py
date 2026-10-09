"""Core Command Pattern Demo"""
from receiver import Light
from commands import LightOnCommand, LightOffCommand
from macro import MacroCommand

def main():
    print("=== Command Pattern Core ===")
    
    # Receiver
    living_room = Light("Living Room")
    kitchen = Light("Kitchen")
    
    # Commands
    living_on = LightOnCommand(living_room)
    living_off = LightOffCommand(living_room)
    kitchen_on = LightOnCommand(kitchen)
    kitchen_off = LightOffCommand(kitchen)
    
    print("\n1. Execute individual commands:")
    living_on.execute()
    kitchen_on.execute()
    
    print("\n2. Macro command:")
    party_mode = MacroCommand()
    party_mode.add(living_on)
    party_mode.add(kitchen_on)
    
    # Turn all off first
    living_off.execute()
    kitchen_off.execute()
    
    print("Execute party mode:")
    party_mode.execute()
    
    print("\n3. Undo:")
    history = MacroCommand()
    history.add(living_off)
    history.add(kitchen_off)
    
    print("Turn lights off:")
    history.execute()
    
    print("Undo last command:")
    history.undo_last()
    print("Replay history:")
    history.execute()
    
    print("\nCore concepts shown:")
    print("• Commands encapsulate requests")
    print("• Invoker decoupled from receiver")
    print("• Commands can be grouped")
    print("• Commands can be undone")

if __name__ == "__main__":
    main()
