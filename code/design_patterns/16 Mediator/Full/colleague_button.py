"""
Mediator Pattern - Concrete Colleague (Button)
A button colleague that can be enabled/disabled by the mediator.
"""

import tkinter as tk
from colleague import Colleague
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mediator import Mediator


class ColleagueButton(tk.Button, Colleague):
    """
    Concrete colleague implementation using tkinter Button.
    The mediator controls when this button is enabled or disabled.
    """
    
    def __init__(self, parent, text: str, **kwargs):
        """
        Initialize the colleague button.
        
        Args:
            parent: The parent tkinter widget
            text (str): The button text
            **kwargs: Additional tkinter Button arguments
        """
        super().__init__(parent, text=text, **kwargs)
        self.mediator: 'Mediator' = None
    
    def set_mediator(self, mediator: 'Mediator'):
        """
        Set the mediator for this button.
        
        Args:
            mediator (Mediator): The mediator to coordinate with
        """
        self.mediator = mediator
    
    def set_colleague_enabled(self, enabled: bool):
        """
        Enable or disable this button.
        
        Args:
            enabled (bool): True to enable, False to disable
        """
        if enabled:
            self.config(state=tk.NORMAL)
        else:
            self.config(state=tk.DISABLED)
