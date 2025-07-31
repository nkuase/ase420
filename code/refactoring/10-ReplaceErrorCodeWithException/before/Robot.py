from Position import Position
from Direction import Direction
from Command import Command

class Robot:
    """Robot class using error codes (before refactoring)"""
    
    def __init__(self, name: str):
        self.name = name
        self.position = Position(0, 0)
        self.direction = Direction(0, 1)
        
    def execute(self, command_sequence: str):
        """Execute a sequence of commands"""
        tokens = command_sequence.split()
        for token in tokens:
            if not self.execute_command(token):
                print(f"Invalid command: {token}")
                break
                
    def execute_command(self, command_string: str) -> bool:
        """Execute command from string, returns False on error"""
        command = Command.parse_command(command_string)
        if command is None:
            return False
        return self._execute_command(command)
        
    def _execute_command(self, command: Command) -> bool:
        """Execute command object, returns False on error"""
        if command == Command.FORWARD:
            self.position.relative_move(self.direction.x, self.direction.y)
        elif command == Command.BACKWARD:
            self.position.relative_move(-self.direction.x, -self.direction.y)
        elif command == Command.TURN_RIGHT:
            self.direction.set_direction(self.direction.y, -self.direction.x)
        elif command == Command.TURN_LEFT:
            self.direction.set_direction(-self.direction.y, self.direction.x)
        else:
            return False
        return True
        
    def __str__(self):
        return (f"[ Robot: {self.name} "
                f"position({self.position.x}, {self.position.y}), "
                f"direction({self.direction.x}, {self.direction.y}) ]")
