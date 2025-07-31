from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtCore import pyqtSignal
from mediator import ColleagueInterface


class ColleagueEntry(QLineEdit):
    """
    A text entry field that participates in the Mediator pattern.
    Uses composition to implement the colleague interface.
    """
    
    def __init__(self, parent=None, echo_mode=None):
        super().__init__(parent)
        self.colleague = ColleagueInterface()
        
        if echo_mode:
            self.setEchoMode(echo_mode)
        
        # Connect text change signal to notify mediator
        self.textChanged.connect(self.notify_mediator)
    
    def set_mediator(self, mediator):
        """Set the mediator that coordinates this entry field."""
        self.colleague.set_mediator(mediator)
    
    def set_colleague_enabled(self, enabled):
        """Enable or disable the entry field based on mediator's coordination logic."""
        self.setEnabled(enabled)
        # Optionally change appearance when disabled
        if enabled:
            self.setStyleSheet("")
        else:
            self.setStyleSheet("background-color: lightgray;")
    
    def notify_mediator(self):
        """Called when text changes - notify the mediator for coordination."""
        self.colleague.notify_mediator()
    
    def get_text(self):
        """Get the current text in the entry field."""
        return self.text()
