"""Simple receiver - knows how to do the work"""

class Light:
    def __init__(self, location):
        self.location = location
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
        print(f"{self.location} light ON")
    
    def turn_off(self):
        self.is_on = False
        print(f"{self.location} light OFF")
