"""
Mediator Pattern - Concrete Colleague (Entry)
An entry field colleague that notifies the mediator when its text changes.
"""

import tkinter as tk
from colleague import Colleague
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mediator import Mediator


class ColleagueEntry(tk.Entry, Colleague):
    """
    Concrete colleague implementation using tkinter Entry.
    Notifies the mediator when its text content changes and
    can be enabled/disabled with visual feedback.
    """
    
    def __init__(self, parent, **kwargs):
        """
        Initialize the colleague entry field.
        
        Args:
            parent: The parent tkinter widget
            **kwargs: Additional tkinter Entry arguments
        """
        super().__init__(parent, **kwargs)
        self.mediator: 'Mediator' = None
        
        # Bind text change events
        self.bind('<KeyRelease>', self._on_text_change)
        self.bind('<FocusOut>', self._on_text_change)
        
        # Store original colors for enable/disable effects
        self.normal_bg = self.cget('bg') or 'white'
        self.disabled_bg = 'lightgray'
    
    def set_mediator(self, mediator: 'Mediator'):
        """
        Set the mediator for this entry field.
        
        Args:
            mediator (Mediator): The mediator to coordinate with
        """
        self.mediator = mediator
    
    def set_colleague_enabled(self, enabled: bool):
        """
        Enable or disable this entry field with visual feedback.
        
        Args:
            enabled (bool): True to enable, False to disable
        """
        if enabled:
            self.config(state=tk.NORMAL, bg=self.normal_bg)
        else:
            self.config(state=tk.DISABLED, bg=self.disabled_bg)
    
    def _on_text_change(self, event=None):
        """Called when the text content changes."""
        if self.mediator:
            self.mediator.colleague_changed()
    
    def get_text(self) -> str:
        """
        Get the current text in the entry field.
        
        Returns:
            str: The current text content
        """
        return self.get()
