class MediatorInterface:
    """
    Interface for mediator objects that coordinate interactions between colleagues.
    Using a regular class instead of ABC to avoid metaclass conflicts with PyQt6.
    """
    
    def create_colleagues(self):
        """Create and initialize all colleague objects."""
        raise NotImplementedError("Subclasses must implement create_colleagues")
    
    def colleague_changed(self):
        """Called when a colleague's state changes and coordination is needed."""
        raise NotImplementedError("Subclasses must implement colleague_changed")


class ColleagueInterface:
    """
    Interface for objects that participate in the Mediator pattern.
    Using composition instead of inheritance to avoid metaclass conflicts with Qt.
    """
    
    def __init__(self):
        self.mediator = None
    
    def set_mediator(self, mediator):
        """Set the mediator that coordinates this colleague."""
        self.mediator = mediator
    
    def set_colleague_enabled(self, enabled):
        """Enable or disable this colleague based on mediator's decision."""
        raise NotImplementedError("Subclasses must implement set_colleague_enabled")
    
    def notify_mediator(self):
        """Notify the mediator when this colleague's state changes."""
        if self.mediator:
            self.mediator.colleague_changed()
