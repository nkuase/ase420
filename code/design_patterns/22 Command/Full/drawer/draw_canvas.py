"""
Command Pattern - Draw Canvas (Receiver)
This class implements the Drawable interface and provides a canvas for drawing.
It also demonstrates how the Command pattern can be used with GUI applications.
"""

import tkinter as tk
from drawer.drawable import Drawable
from command.macro_command import MacroCommand


class DrawCanvas(tk.Canvas, Drawable):
    """
    Concrete receiver that implements the drawing functionality.
    This canvas can draw circles and maintains a history of drawing commands.
    """
    
    def __init__(self, parent, width: int, height: int, history: MacroCommand):
        """
        Initialize the drawing canvas.
        
        Args:
            parent: The parent tkinter widget
            width (int): Canvas width
            height (int): Canvas height
            history (MacroCommand): Command history for redrawing
        """
        super().__init__(parent, width=width, height=height, bg='white')
        self.width = width
        self.height = height
        self.history = history
        self.color = 'red'
        self.radius = 6
        
        # Bind mouse events for drawing
        self.bind('<B1-Motion>', self._on_mouse_drag)
        self.bind('<Button-1>', self._on_mouse_click)
        
        # Make canvas focusable
        self.focus_set()
    
    def draw(self, x: int, y: int):
        """
        Draw a circle at the specified coordinates.
        
        Args:
            x (int): X coordinate
            y (int): Y coordinate
        """
        # Draw a filled circle (oval)
        x1 = x - self.radius
        y1 = y - self.radius
        x2 = x + self.radius
        y2 = y + self.radius
        
        self.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)
    
    def _on_mouse_click(self, event):
        """Handle single mouse click."""
        # Import here to avoid circular dependency
        from drawer.draw_command import DrawCommand
        
        cmd = DrawCommand(self, event.x, event.y)
        self.history.append(cmd)
        cmd.execute()
    
    def _on_mouse_drag(self, event):
        """Handle mouse drag for continuous drawing."""
        # Import here to avoid circular dependency
        from drawer.draw_command import DrawCommand
        
        cmd = DrawCommand(self, event.x, event.y)
        self.history.append(cmd)
        cmd.execute()
    
    def repaint(self):
        """
        Repaint the canvas by clearing it and executing all commands in history.
        This demonstrates how commands can be replayed.
        """
        self.delete("all")  # Clear canvas
        self.history.execute()  # Replay all commands
    
    def set_color(self, color: str):
        """
        Set the drawing color.
        
        Args:
            color (str): Color name or hex value
        """
        self.color = color
    
    def set_radius(self, radius: int):
        """
        Set the drawing radius.
        
        Args:
            radius (int): Circle radius in pixels
        """
        self.radius = radius
    
    def get_drawing_info(self) -> dict:
        """
        Get current drawing settings.
        
        Returns:
            dict: Current color and radius settings
        """
        return {
            'color': self.color,
            'radius': self.radius,
            'commands': self.history.size()
        }
