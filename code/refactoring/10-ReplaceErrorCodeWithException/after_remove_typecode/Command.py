from typing import Dict
from InvalidCommandException import InvalidCommandException

class Command:
    """Command class with constant instances (exception version)"""
    
    def __init__(self, name: str):
        self._name = name
        
    def get_name(self) -> str:
        return self._name
        
    def execute(self, robot) -> None: pass
        
    @staticmethod
    def parse_command(name: str) -> 'Command':
        """Parse command from string, throws exception if invalid"""
        if name not in Command._command_name_map:
            raise InvalidCommandException(name)
        return Command._command_name_map[name]
        
class Forward(Command):
    def __init__(self):
        super().__init__("forward")
        
    def execute(self, robot) -> None:
        robot.forward()        

class Backward(Command):
    def __init__(self):
        super().__init__("backward")
        
    def execute(self, robot) -> None:
        robot.backward()   

class Left(Command):
    def __init__(self):
        super().__init__("left")
        
    def execute(self, robot) -> None:
        robot.left()  
        
class Right(Command):
    def __init__(self):
        super().__init__("right")
        
    def execute(self, robot) -> None:
        robot.right()          

# Command name mapping
Command._command_name_map: Dict[str, Command] = {
    "forward": Forward(),
    "backward": Backward(),
    "right": Right(),
    "left": Left()
}
