from PyQt6.QtWidgets import QPushButton
from mediator import ColleagueInterface


class ColleagueButton(QPushButton):
    """
    A button that participates in the Mediator pattern.
    Uses composition to implement the colleague interface.
    """
    
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.colleague = ColleagueInterface()
    
    def set_mediator(self, mediator):
        """Set the mediator and register this button as a colleague."""
        self.colleague.set_mediator(mediator)
    
    def set_colleague_enabled(self, enabled):
        """Enable or disable the button based on mediator's coordination logic."""
        self.setEnabled(enabled)
    
    def notify_mediator(self):
        """Notify the mediator when this button's state changes."""
        self.colleague.notify_mediator()
