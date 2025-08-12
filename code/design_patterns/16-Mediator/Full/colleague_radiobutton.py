"""
Mediator Pattern - Concrete Colleague (Radiobutton)
A radiobutton colleague that notifies the mediator when its state changes.
"""

import tkinter as tk
from colleague import Colleague
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mediator import Mediator


class ColleagueRadiobutton(tk.Radiobutton, Colleague):
    """
    Concrete colleague implementation using tkinter Radiobutton.
    Notifies the mediator when its selection state changes.
    """
    
    def __init__(self, parent, text: str, variable: tk.Variable, value, **kwargs):
        """
        Initialize the colleague radiobutton.
        
        Args:
            parent: The parent tkinter widget
            text (str): The radiobutton text
            variable (tk.Variable): The tkinter variable to track selection
            value: The value this radiobutton represents
            **kwargs: Additional tkinter Radiobutton arguments
        """
        super().__init__(parent, text=text, variable=variable, value=value, **kwargs)
        self.mediator: 'Mediator' = None
        self.variable = variable
        
        # Configure the command to notify mediator
        self.config(command=self._on_change)
    
    def set_mediator(self, mediator: 'Mediator'):
        """
        Set the mediator for this radiobutton.
        
        Args:
            mediator (Mediator): The mediator to coordinate with
        """
        self.mediator = mediator
    
    def set_colleague_enabled(self, enabled: bool):
        """
        Enable or disable this radiobutton.
        
        Args:
            enabled (bool): True to enable, False to disable
        """
        if enabled:
            self.config(state=tk.NORMAL)
        else:
            self.config(state=tk.DISABLED)
    
    def _on_change(self):
        """Called when the radiobutton state changes."""
        if self.mediator:
            self.mediator.colleague_changed()
    
    def get_state(self) -> bool:
        """
        Check if this radiobutton is selected.
        
        Returns:
            bool: True if selected, False otherwise
        """
        return self.variable.get() == self.cget('value')
