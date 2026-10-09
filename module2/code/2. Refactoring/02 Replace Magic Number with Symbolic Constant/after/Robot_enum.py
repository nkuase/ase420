from enum import Enum

class Robot:
    """Robot using enum for type-safe commands"""
    
    class Command(Enum):
        WALK = "walk"
        STOP = "stop" 
        JUMP = "jump"
    
    def __init__(self, name):
        self._name = name
    
    def order(self, command):
        if command == self.Command.WALK:
            print(f"{self._name} walks.")
        elif command == self.Command.STOP:
            print(f"{self._name} stops.")
        elif command == self.Command.JUMP:
            print(f"{self._name} jumps.")
        else:
            print(f"Command error. command = {command}")
