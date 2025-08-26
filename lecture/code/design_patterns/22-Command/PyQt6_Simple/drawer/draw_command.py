from command.command import Command
from drawer.drawable import Drawable

class DrawCommand(Command):
    """
    Concrete implementation of the Command pattern for drawing operations.
    
    DrawCommand encapsulates a drawing request as an object. It stores:
    - The receiver (drawable object) that will perform the drawing
    - The parameters (x, y coordinates) needed for the operation
    
    This demonstrates key Command pattern concepts:
    - Encapsulation: The request is wrapped in an object
    - Parameterization: Different coordinates create different commands
    - Queuing: Commands can be stored and executed later
    - Logging: Command history can be maintained
    - Undo: Commands can be removed from history
    
    Real-world applications:
    - Drawing/CAD applications (like this example)
    - Text editors (insert, delete, format commands)
    - Database transactions (SQL commands)
    - Remote procedure calls (network commands)
    - Macro recording in applications
    """
    
    def __init__(self, drawable, x, y, color='red', radius=6):
        """
        Initialize the draw command.
        
        Args:
            drawable (Drawable): The object that will perform the drawing
            x (int): X-coordinate for the drawing operation
            y (int): Y-coordinate for the drawing operation
            color (str): Color to use for drawing (stored for accurate replay)
            radius (int): Radius to use for drawing (stored for accurate replay)
            
        Raises:
            TypeError: If drawable doesn't implement the Drawable interface
            ValueError: If coordinates are not valid numbers
        """
        if not isinstance(drawable, Drawable):
            raise TypeError(f"Expected Drawable instance, got {type(drawable).__name__}")
        
        try:
            self.drawable = drawable
            self.x = int(x)
            self.y = int(y)
            self.color = color
            self.radius = radius
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid coordinates: x={x}, y={y}") from e
        
        # Optional: Store timestamp for debugging/logging
        import time
        self.created_at = time.time()
    
    def execute(self):
        """
        Execute the drawing command.
        
        This method demonstrates the core of the Command pattern:
        the command knows which receiver to call and what parameters to pass.
        The invoker (GUI) doesn't need to know these details.
        
        For accurate replay, this command temporarily sets the drawing state
        to match what was active when the command was created.
        """
        # Save current drawing state
        if hasattr(self.drawable, 'get_drawing_state'):
            saved_state = self.drawable.get_drawing_state()
            
            # Set the state that was active when this command was created
            self.drawable.set_drawing_state(self.color, self.radius)
            
            # Execute the drawing operation
            self.drawable.draw(self.x, self.y)
            
            # Restore the previous state
            self.drawable.set_drawing_state(saved_state['color'], saved_state['radius'])
        else:
            # Fallback for simple drawables that don't support state management
            self.drawable.draw(self.x, self.y)
    
    def get_position(self):
        """
        Get the coordinates associated with this command.
        
        Returns:
            tuple: (x, y) coordinates as a tuple
            
        This method provides access to the command's parameters without
        exposing the internal implementation. Useful for debugging,
        logging, or advanced undo/redo implementations.
        """
        return (self.x, self.y)
    
    def get_receiver(self):
        """
        Get the receiver object for this command.
        
        Returns:
            Drawable: The drawable object that performs the drawing
            
        Useful for introspection and debugging.
        """
        return self.drawable
    
    def __str__(self):
        """
        String representation of the command for debugging.
        
        Returns:
            str: Human-readable description of the command
        """
        return f"DrawCommand(x={self.x}, y={self.y}, color={self.color}, radius={self.radius})"
    
    def __repr__(self):
        """
        Detailed string representation for debugging.
        
        Returns:
            str: Detailed representation including receiver type
        """
        receiver_type = type(self.drawable).__name__
        return f"DrawCommand(receiver={receiver_type}, x={self.x}, y={self.y}, color={self.color}, radius={self.radius})"
    
    def __eq__(self, other):
        """
        Compare two DrawCommand instances for equality.
        
        Args:
            other: Another object to compare with
            
        Returns:
            bool: True if both commands have the same coordinates, color, radius and receiver
        """
        if not isinstance(other, DrawCommand):
            return False
        
        return (self.x == other.x and 
                self.y == other.y and 
                self.color == other.color and
                self.radius == other.radius and
                self.drawable is other.drawable)
    
    def __hash__(self):
        """
        Make DrawCommand hashable so it can be stored in sets or used as dict keys.
        
        Returns:
            int: Hash value based on coordinates, drawing state and receiver
        """
        return hash((self.x, self.y, self.color, self.radius, id(self.drawable)))
    
    def distance_from(self, other_command):
        """
        Calculate distance from another DrawCommand.
        
        Args:
            other_command (DrawCommand): Another draw command
            
        Returns:
            float: Euclidean distance between the two commands
            
        Useful for optimizations like command clustering or path smoothing.
        """
        if not isinstance(other_command, DrawCommand):
            raise TypeError("Can only calculate distance to another DrawCommand")
        
        dx = self.x - other_command.x
        dy = self.y - other_command.y
        return (dx * dx + dy * dy) ** 0.5
