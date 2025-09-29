from State import State

class StateLogging(State):
    def start(self):
        pass
            
    def stop(self):
        print("** STOP LOGGING **")
            
    def log(self, info: str):
        print(f"Logging: {info}")
