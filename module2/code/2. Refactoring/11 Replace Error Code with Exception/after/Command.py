from typing import Dict
from InvalidCommandException import InvalidCommandException

class Command:
    """Command class with constant instances (exception version)"""
    
    def __init__(self, name: str):
        self._name = name
        
    def get_name(self) -> str:
        return self._name
        
    @staticmethod
    def parse_command(name: str) -> 'Command':
        """Parse command from string, throws exception if invalid"""
        if name not in Command._command_name_map:
            raise InvalidCommandException(name)
        return Command._command_name_map[name]

# Create command constants
Command.FORWARD = Command("forward")
Command.BACKWARD = Command("backward")
Command.TURN_RIGHT = Command("right")
Command.TURN_LEFT = Command("left")

# Command name mapping
Command._command_name_map: Dict[str, Command] = {
    "forward": Command.FORWARD,
    "backward": Command.BACKWARD,
    "right": Command.TURN_RIGHT,
    "left": Command.TURN_LEFT
}
