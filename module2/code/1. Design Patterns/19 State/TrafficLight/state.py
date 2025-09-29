class TrafficLightState:  # State
    def handle(self, light):
        pass

class RedState(TrafficLightState):  # ConcreteState
    def handle(self, light):
        print("Red light - Stop!")
        light.set_state(GreenState()) # next state is green
        
class GreenState(TrafficLightState):  # ConcreteState
    def handle(self, light):
        print("Green light - Go!")
        light.set_state(RedState())        