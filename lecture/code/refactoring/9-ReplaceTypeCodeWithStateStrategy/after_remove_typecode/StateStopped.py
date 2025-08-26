from State import State

class StateStopped(State):
    def start(self):
        print("** START LOGGING **")
            
    def stop(self): pass
            
    def log(self, info: str): 
        print(f"Ignoring: {info}")
