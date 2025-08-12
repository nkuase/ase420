from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor
from drawer.drawable import Drawable


class DrawCanvas(QWidget, Drawable):
    """
    PyQt6 implementation of a drawing canvas that demonstrates the Command pattern.
    
    This class serves as both the receiver (implements Drawable) and the user interface
    for drawing operations. Each mouse click/drag creates a DrawCommand that gets
    stored in the command history for undo/redo functionality.
    """
    
    def __init__(self, width, height, history):
        super().__init__()
        self.canvas_width = width
        self.canvas_height = height
        self.history = history
        self.color = 'red'
        self.radius = 6
        
        # List to store drawn points for visual rendering
        self.drawn_points = []
        
        # Set up the widget
        self.setFixedSize(width, height)
        self.setStyleSheet("background-color: white; border: 1px solid black;")
        
        # Enable mouse tracking for drag events
        self.setMouseTracking(False)  # Only track when button is pressed
    
    def draw(self, x, y):
        """
        Implementation of Drawable interface.
        Adds a point to the internal list for rendering.
        This method is called by DrawCommand.execute()
        """
        # Store the point with current color for rendering
        point_data = {
            'x': x,
            'y': y,
            'color': self.color,
            'radius': self.radius
        }
        self.drawn_points.append(point_data)
        
        # Trigger a repaint of the widget
        self.update()
    
    def paintEvent(self, event):
        """
        PyQt6 paint event handler.
        This method is called automatically when the widget needs to be redrawn.
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Draw all stored points
        for point in self.drawn_points:
            # Set up the painter for this point
            color = QColor(point['color'])
            painter.setPen(QPen(color, 1))
            painter.setBrush(QBrush(color))
            
            # Draw the circle
            x = point['x']
            y = point['y']
            radius = point['radius']
            painter.drawEllipse(x - radius, y - radius, radius * 2, radius * 2)
    
    def mousePressEvent(self, event):
        """Handle mouse press events (start of drawing)"""
        if event.button() == Qt.MouseButton.LeftButton:
            self._create_and_execute_command(event.position().x(), event.position().y())
    
    def mouseMoveEvent(self, event):
        """Handle mouse move events (dragging)"""
        if event.buttons() & Qt.MouseButton.LeftButton:
            self._create_and_execute_command(event.position().x(), event.position().y())
    
    def _create_and_execute_command(self, x, y):
        """
        Create a DrawCommand for the given position and execute it.
        This demonstrates the Command pattern in action.
        
        The command stores the current drawing state (color, radius) so that
        it can be accurately replayed later.
        """
        from drawer.draw_command import DrawCommand
        
        # Create the command with current drawing state (encapsulating the request)
        cmd = DrawCommand(self, int(x), int(y), self.color, self.radius)
        
        # Add to history (for undo/redo functionality)
        self.history.append(cmd)
        
        # Execute the command
        cmd.execute()
        
        print(f"Created and executed DrawCommand at ({int(x)}, {int(y)}) with color={self.color}, radius={self.radius}")
    
    def repaint(self):
        """
        Clear the canvas and replay all commands from history.
        This demonstrates the replay capability of the Command pattern.
        
        Added educational delay so you can see the clearing and redrawing process.
        """
        print(f"Starting repaint with {self.history.size()} commands...")
        
        if self.history.is_empty():
            print("No commands in history to repaint")
            return
        
        # Clear current visual state
        self.clear_canvas()
        
        # Add a visible delay so user can see the clearing
        print("Canvas cleared - waiting 1 second before redrawing...")
        
        # Use QTimer to create a visible delay
        QTimer.singleShot(1000, self._replay_commands_delayed)
        
    def _replay_commands_delayed(self):
        """
        Replay commands after the visual delay.
        This makes the repaint process educational and visible.
        """
        print("Now replaying commands one by one...")
        
        commands = list(self.history.get_commands())
        self._replay_index = 0
        self._commands_to_replay = commands
        
        # Start replaying commands with delays between them
        self._replay_next_command()
    
    def _replay_next_command(self):
        """
        Replay the next command in sequence with a small delay.
        This makes the rebuild process visible and educational.
        """
        if self._replay_index < len(self._commands_to_replay):
            cmd = self._commands_to_replay[self._replay_index]
            print(f"  Replaying command {self._replay_index + 1}/{len(self._commands_to_replay)}: {cmd}")
            
            cmd.execute()
            self._replay_index += 1
            
            # Schedule next command with a small delay
            QTimer.singleShot(200, self._replay_next_command)
        else:
            print(f"Repaint completed! Recreated {len(self.drawn_points)} points from command history.")
            print("This demonstrates how the Command pattern enables perfect replay of operations!")
    
    def clear_canvas(self):
        """Clear the visual representation of the canvas"""
        self.drawn_points.clear()
        self.update()  # Trigger repaint
    
    def set_color(self, color):
        """Set the current drawing color"""
        self.color = color
        print(f"Canvas drawing color set to: {color}")
    
    def set_radius(self, radius):
        """Set the current drawing radius"""
        self.radius = radius
        print(f"Canvas drawing radius set to: {radius}")
    
    def get_drawing_state(self):
        """
        Get the current drawing state.
        
        Returns:
            dict: Current color and radius settings
        """
        return {
            'color': self.color,
            'radius': self.radius
        }
    
    def set_drawing_state(self, color, radius):
        """
        Set the drawing state (used by commands for accurate replay).
        
        Args:
            color (str): Color to set
            radius (int): Radius to set
        """
        self.color = color
        self.radius = radius
    
    def get_drawing_info(self):
        """Get current drawing configuration information"""
        return {
            'color': self.color,
            'radius': self.radius,
            'commands': self.history.size(),
            'points_drawn': len(self.drawn_points)
        }
    
    def get_canvas_size(self):
        """Get the canvas dimensions"""
        return (self.canvas_width, self.canvas_height)
