class Robot:
    """Robot class with magic numbers (before refactoring)"""
    
    def __init__(self, name: str):
        self.name = name
        
    def order(self, command: int):
        if command == 0:  # Magic number!
            print(f"{self.name} walks.")
        elif command == 1:  # Magic number!
            print(f"{self.name} stops.")
        elif command == 2:  # Magic number!
            print(f"{self.name} jumps.")
        else:
            print(f"Command error. command = {command}")
