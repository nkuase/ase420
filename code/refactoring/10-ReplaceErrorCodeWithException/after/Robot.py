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
        self._execute_command(command)
        
    def _execute_command(self, command: Command):
        """Execute command object, throws exception on error"""
        if command == Command.FORWARD:
            self.position.relative_move(self.direction.x, self.direction.y)
        elif command == Command.BACKWARD:
            self.position.relative_move(-self.direction.x, -self.direction.y)
        elif command == Command.TURN_RIGHT:
            self.direction.set_direction(self.direction.y, -self.direction.x)
        elif command == Command.TURN_LEFT:
            self.direction.set_direction(-self.direction.y, self.direction.x)
        else:
            raise InvalidCommandException()
        
    def __str__(self):
        return (f"[ Robot: {self.name} "
                f"position({self.position.x}, {self.position.y}), "
                f"direction({self.direction.x}, {self.direction.y}) ]")
