class Robot:
    """Robot class with symbolic constants (after refactoring)"""
    
    COMMAND_WALK = 0
    COMMAND_STOP = 1
    COMMAND_JUMP = 2
    
    def __init__(self, name: str):
        self.name = name
        
    def order(self, command: int):
        if command == Robot.COMMAND_WALK:
            print(f"{self.name} walks.")
        elif command == Robot.COMMAND_STOP:
            print(f"{self.name} stops.")
        elif command == Robot.COMMAND_JUMP:
            print(f"{self.name} jumps.")
        else:
            print(f"Command error. command = {command}")
