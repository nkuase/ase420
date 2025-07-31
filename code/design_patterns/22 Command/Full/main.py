"""
Command Pattern Demo
This example demonstrates the Command pattern through a simple drawing application
where each drawing operation is encapsulated as a command object.

Key concepts demonstrated:
1. Encapsulating requests as objects
2. Parameterizing objects with different requests
3. Queuing operations and supporting undo
4. Logging and replaying operations
"""

import tkinter as tk
from tkinter import ttk
from command.macro_command import MacroCommand
from drawer.draw_canvas import DrawCanvas


class DrawingApp:
    """
    Main application that demonstrates the Command pattern.
    Provides a GUI for drawing with command-based operations.
    """
    
    def __init__(self):
        """Initialize the drawing application."""
        self.root = tk.Tk()
        self.root.title("Command Pattern Demo - Drawing App")
        self.root.resizable(False, False)
        
        # Command history
        self.history = MacroCommand()
        
        # Create GUI components
        self._create_widgets()
        self._setup_layout()
        
        # Center the window
        self._center_window()
    
    def _create_widgets(self):
        """Create all GUI widgets."""
        # Main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        
        # Info label
        self.info_label = ttk.Label(
            self.main_frame, 
            text="Click and drag to draw. Each stroke is a command that can be undone or replayed.",
            font=('Arial', 10)
        )
        
        # Drawing canvas
        self.canvas = DrawCanvas(self.main_frame, 500, 400, self.history)
        
        # Control buttons frame
        self.button_frame = ttk.Frame(self.main_frame)
        
        # Buttons
        self.clear_button = ttk.Button(
            self.button_frame, text="Clear All", command=self._clear_canvas
        )
        self.undo_button = ttk.Button(
            self.button_frame, text="Undo Last", command=self._undo_last
        )
        self.repaint_button = ttk.Button(
            self.button_frame, text="Repaint", command=self._repaint_canvas
        )
        
        # Color selection
        self.color_frame = ttk.Frame(self.main_frame)
        ttk.Label(self.color_frame, text="Color:").pack(side=tk.LEFT, padx=(0, 5))
        
        self.color_var = tk.StringVar(value="red")
        colors = ["red", "blue", "green", "black", "purple", "orange"]
        self.color_combo = ttk.Combobox(
            self.color_frame, textvariable=self.color_var, 
            values=colors, state="readonly", width=8
        )
        self.color_combo.bind('<<ComboboxSelected>>', self._on_color_change)
        
        # Status label
        self.status_label = ttk.Label(
            self.main_frame, text="Commands in history: 0", 
            font=('Arial', 9), foreground='gray'
        )
        
        # Start status update timer
        self._update_status()
    
    def _setup_layout(self):
        """Set up the GUI layout."""
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.info_label.pack(pady=(0, 10))
        self.canvas.pack(pady=(0, 10))
        
        self.color_frame.pack(pady=(0, 5))
        self.color_combo.pack(side=tk.LEFT)
        
        self.button_frame.pack(pady=(0, 10))
        self.clear_button.pack(side=tk.LEFT, padx=(0, 5))
        self.undo_button.pack(side=tk.LEFT, padx=(0, 5))
        self.repaint_button.pack(side=tk.LEFT)
        
        self.status_label.pack()
    
    def _center_window(self):
        """Center the window on the screen."""
        self.root.update_idletasks()
        width = self.root.winfo_reqwidth()
        height = self.root.winfo_reqheight()
        pos_x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        pos_y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
    
    def _clear_canvas(self):
        """Clear the canvas and command history."""
        self.history.clear()
        self.canvas.delete("all")
        print("Canvas cleared - all commands removed from history")
    
    def _undo_last(self):
        """Undo the last command and repaint."""
        if not self.history.is_empty():
            self.history.undo()
            self.canvas.repaint()
            print("Last command undone")
        else:
            print("No commands to undo")
    
    def _repaint_canvas(self):
        """Repaint the canvas by replaying all commands."""
        print(f"Repainting canvas with {self.history.size()} commands...")
        self.canvas.repaint()
        print("Repaint completed")
    
    def _on_color_change(self, event=None):
        """Handle color selection change."""
        new_color = self.color_var.get()
        self.canvas.set_color(new_color)
        print(f"Drawing color changed to: {new_color}")
    
    def _update_status(self):
        """Update the status label with current command count."""
        count = self.history.size()
        self.status_label.config(text=f"Commands in history: {count}")
        
        # Update button states
        has_commands = not self.history.is_empty()
        self.undo_button.config(state=tk.NORMAL if has_commands else tk.DISABLED)
        self.repaint_button.config(state=tk.NORMAL if has_commands else tk.DISABLED)
        
        # Schedule next update
        self.root.after(100, self._update_status)
    
    def run(self):
        """Start the application."""
        self.root.mainloop()


def demonstrate_command_pattern():
    """
    Demonstrate the Command pattern concepts without GUI.
    """
    print("=== Command Pattern Concepts ===")
    
    # Create a simple drawable receiver
    class SimpleDrawable:
        def __init__(self):
            self.points = []
        
        def draw(self, x, y):
            self.points.append((x, y))
            print(f"Drew point at ({x}, {y})")
        
        def get_points(self):
            return self.points.copy()
        
        def clear(self):
            self.points.clear()
    
    # Import command classes
    from drawer.draw_command import DrawCommand
    
    print("\n1. Creating receiver and commands...")
    drawable = SimpleDrawable()
    
    # Create individual commands
    cmd1 = DrawCommand(drawable, 10, 20)
    cmd2 = DrawCommand(drawable, 30, 40)
    cmd3 = DrawCommand(drawable, 50, 60)
    
    print("\n2. Executing individual commands...")
    cmd1.execute()
    cmd2.execute()
    cmd3.execute()
    
    print(f"Points drawn: {drawable.get_points()}")
    
    print("\n3. Creating and executing macro command...")
    macro = MacroCommand()
    macro.append(DrawCommand(drawable, 70, 80))
    macro.append(DrawCommand(drawable, 90, 100))
    
    print("Executing macro command:")
    macro.execute()
    
    print(f"All points: {drawable.get_points()}")
    
    print("\n4. Demonstrating undo functionality...")
    print(f"Macro size before undo: {macro.size()}")
    macro.undo()
    print(f"Macro size after undo: {macro.size()}")
    
    print("\n5. Clearing drawable and replaying macro...")
    drawable.clear()
    print("Replaying remaining macro commands:")
    macro.execute()
    print(f"Final points: {drawable.get_points()}")


def main():
    """
    Main function that demonstrates the Command pattern.
    """
    print("=== Command Pattern Demo ===\n")
    
    print("The Command pattern encapsulates requests as objects,")
    print("allowing you to parameterize clients with different requests,")
    print("queue operations, and support undo functionality.\n")
    
    # Demonstrate concepts
    demonstrate_command_pattern()
    
    print(f"\n{'='*60}")
    print("Starting GUI Demo...")
    print("Instructions:")
    print("- Click and drag on the canvas to draw")
    print("- Each drawing operation creates a command")
    print("- Use 'Undo Last' to remove the most recent command")
    print("- Use 'Repaint' to clear and replay all commands")
    print("- Use 'Clear All' to remove all commands")
    print("- Change colors to see different drawing effects")
    print(f"{'='*60}")
    
    try:
        app = DrawingApp()
        app.run()
    except KeyboardInterrupt:
        print("\nDemo interrupted by user")
    except Exception as e:
        print(f"Error running GUI demo: {e}")
        print("Note: This demo requires a GUI environment with tkinter support")
    
    print("\nCommand Pattern Benefits Demonstrated:")
    print("✅ Encapsulation: Each request is wrapped in a command object")
    print("✅ Parameterization: Commands can be stored and passed around")
    print("✅ Queuing: Commands can be collected in macro commands")
    print("✅ Undo/Redo: Commands can be undone by removing from history")
    print("✅ Logging: Command history provides a log of all operations")
    print("✅ Replay: Commands can be re-executed for redrawing")
    
    print("\nKey Points:")
    print("- Command interface defines execute() method")
    print("- Concrete commands encapsulate receiver and action")
    print("- Invoker (GUI) doesn't need to know command details")
    print("- Receiver (DrawCanvas) performs the actual work")
    print("- MacroCommand demonstrates Composite pattern integration")
    print("- Supports undo by maintaining command history")


if __name__ == "__main__":
    main()
