from typing import Optional, Dict

class Command:
    """Command class with constant instances"""
    
    def __init__(self, name: str):
        self._name = name
        
    def get_name(self) -> str:
        return self._name
        
    @staticmethod
    def parse_command(name: str) -> Optional['Command']:
        """Parse command from string, returns None if invalid"""
        return Command._command_name_map.get(name)

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
