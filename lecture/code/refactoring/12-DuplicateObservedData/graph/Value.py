from ValueChangeEvent import ValueChangeEvent

class Value:
    """Observable value class that notifies listeners of changes"""
    
    def __init__(self, value=0):
        self.value = value
        self.listeners = []
        
    def set_value(self, value):
        self.value = value
        self.notify_listeners()
        
    def get_value(self):
        return self.value
        
    def add_value_listener(self, listener):
        self.listeners.append(listener)
        
    def remove_value_listener(self, listener):
        if listener in self.listeners:
            self.listeners.remove(listener)
            return True
        return False
        
    def notify_listeners(self):
        event = ValueChangeEvent(self)
        for listener in self.listeners:
            listener.value_changed(event)
