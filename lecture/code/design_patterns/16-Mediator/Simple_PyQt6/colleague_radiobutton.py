from PyQt6.QtWidgets import QRadioButton
from mediator import ColleagueInterface


class ColleagueRadioButton(QRadioButton):
    """
    A radio button that participates in the Mediator pattern.
    Uses composition to implement the colleague interface.
    """
    
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.colleague = ColleagueInterface()
        
        # Connect toggle signal to notify mediator
        self.toggled.connect(self._on_toggle)
    
    def set_mediator(self, mediator):
        """Set the mediator that coordinates this radio button."""
        self.colleague.set_mediator(mediator)
    
    def set_colleague_enabled(self, enabled):
        """Enable or disable the radio button based on mediator's coordination logic."""
        self.setEnabled(enabled)
    
    def _on_toggle(self, checked):
        """Called when radio button is toggled - notify the mediator for coordination."""
        if checked:  # Only notify when becoming checked (not unchecked)
            self.notify_mediator()
    
    def notify_mediator(self):
        """Notify the mediator when this radio button's state changes."""
        self.colleague.notify_mediator()
    
    def get_state(self):
        """Get the current state of the radio button."""
        return self.isChecked()
