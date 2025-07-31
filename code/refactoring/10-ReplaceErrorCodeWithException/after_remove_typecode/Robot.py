from Position import Position
from Direction import Direction
from Command import Command
from InvalidCommandException import InvalidCommandException

class Robot:
    """Robot class using exceptions (after refactoring)"""
    
    def __init__(self, name: str):
        self.name = name
        self.position = Position(0, 0)
        self.direction = Direction(0, 1)
        
    def execute(self, command_sequence: str):
        """Execute a sequence of commands"""
        tokens = command_sequence.split()
        try:
            for token in tokens:
                self.execute_command(token)
        except InvalidCommandException as e:
            print(f"Invalid command: {e.message}")
            
    def execute_command(self, command_string: str):
        """Execute command from string, throws exception on error"""
        command = Command.parse_command(command_string)
        command.execute(self)
        
    def forward(self):
        self.position.relative_move(self.direction.x, self.direction.y)
    def backward(self):
        self.position.relative_move(-self.direction.x, -self.direction.y)
    def right(self):
        self.direction.set_direction(self.direction.y, -self.direction.x)
    def left(self):
        self.direction.set_direction(-self.direction.y, self.direction.x)
        
    def __str__(self):
        return (f"[ Robot: {self.name} "
                f"position({self.position.x}, {self.position.y}), "
                f"direction({self.direction.x}, {self.direction.y}) ]")
