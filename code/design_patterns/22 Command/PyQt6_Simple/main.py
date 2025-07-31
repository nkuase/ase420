import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                             QWidget, QPushButton, QLabel, QComboBox, QFrame)
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont
from command.macro_command import MacroCommand
from drawer.draw_canvas import DrawCanvas

class DrawingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Command Pattern Demo - Drawing App (PyQt6)")
        self.setFixedSize(640, 600)
        
        self.history = MacroCommand()
        
        self._create_widgets()
        self._setup_layout()
        self._center_window()
        
        # Timer to update status periodically
        self.status_timer = QTimer()
        self.status_timer.timeout.connect(self._update_status)
        self.status_timer.start(100)  # Update every 100ms
    
    def _create_widgets(self):
        # Central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Info label
        self.info_label = QLabel(
            "Click and drag to draw. Each stroke is a command that can be undone or replayed."
        )
        self.info_label.setFont(QFont("Arial", 10))
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info_label.setWordWrap(True)
        
        # Drawing canvas
        self.canvas = DrawCanvas(500, 400, self.history)
        
        # Color selection frame
        self.color_frame = QFrame()
        self.color_label = QLabel("Color:")
        
        self.color_combo = QComboBox()
        colors = ["red", "blue", "green", "black", "purple", "orange"]
        self.color_combo.addItems(colors)
        self.color_combo.setCurrentText("red")
        self.color_combo.currentTextChanged.connect(self._on_color_change)
        
        # Button frame
        self.button_frame = QFrame()
        
        self.clear_button = QPushButton("Clear All")
        self.clear_button.clicked.connect(self._clear_canvas)
        
        self.undo_button = QPushButton("Undo Last")
        self.undo_button.clicked.connect(self._undo_last)
        
        self.repaint_button = QPushButton("Repaint")
        self.repaint_button.clicked.connect(self._repaint_canvas)
        
        # Status label
        self.status_label = QLabel("Commands in history: 0")
        self.status_label.setFont(QFont("Arial", 9))
        self.status_label.setStyleSheet("color: gray;")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self._update_status()
    
    def _setup_layout(self):
        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)
        
        # Add info label
        main_layout.addWidget(self.info_label)
        
        # Add canvas
        main_layout.addWidget(self.canvas, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Color selection layout
        color_layout = QHBoxLayout()
        color_layout.addWidget(self.color_label)
        color_layout.addWidget(self.color_combo)
        color_layout.addStretch()
        self.color_frame.setLayout(color_layout)
        main_layout.addWidget(self.color_frame)
        
        # Button layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.clear_button)
        button_layout.addWidget(self.undo_button)
        button_layout.addWidget(self.repaint_button)
        self.button_frame.setLayout(button_layout)
        main_layout.addWidget(self.button_frame)
        
        # Add status label
        main_layout.addWidget(self.status_label)
        
        self.central_widget.setLayout(main_layout)
    
    def _center_window(self):
        """Center the window on the screen"""
        screen = QApplication.primaryScreen().geometry()
        window = self.frameGeometry()
        center_point = screen.center()
        window.moveCenter(center_point)
        self.move(window.topLeft())
    
    def _clear_canvas(self):
        """Clear all commands and the canvas"""
        self.history.clear()
        self.canvas.clear_canvas()
        print("Canvas cleared - all commands removed from history")
    
    def _undo_last(self):
        """Undo the last command"""
        if not self.history.is_empty():
            self.history.undo()
            self.canvas.repaint()
            print("Last command undone")
        else:
            print("No commands to undo")
    
    def _repaint_canvas(self):
        """Repaint the canvas using all commands in history"""
        print(f"Repainting canvas with {self.history.size()} commands...")
        self.canvas.repaint()
        print("Repaint completed")
    
    def _on_color_change(self, color):
        """Handle color change from combo box"""
        self.canvas.set_color(color)
        print(f"Drawing color changed to: {color}")
    
    def _update_status(self):
        """Update the status label and button states"""
        count = self.history.size()
        self.status_label.setText(f"Commands in history: {count}")
        
        has_commands = not self.history.is_empty()
        self.undo_button.setEnabled(has_commands)
        self.repaint_button.setEnabled(has_commands)


def demonstrate_command_pattern():
    """Demonstrate Command pattern concepts without GUI"""
    print("=== Command Pattern Concepts ===")
    
    # Import the Drawable interface
    from drawer.drawable import Drawable
    
    class SimpleDrawable(Drawable):
        """
        Simple implementation of Drawable for console demonstration.
        This shows how any class can implement the Drawable interface.
        """
        def __init__(self):
            self.points = []
        
        def draw(self, x, y):
            """Implementation of the abstract draw method"""
            self.points.append((x, y))
            print(f"Drew point at ({x}, {y})")
        
        def get_points(self):
            return self.points.copy()
        
        def clear(self):
            self.points.clear()
    
    from drawer.draw_command import DrawCommand
    
    print("\n1. Creating receiver and commands...")
    drawable = SimpleDrawable()
    
    cmd1 = DrawCommand(drawable, 10, 20, 'red', 6)
    cmd2 = DrawCommand(drawable, 30, 40, 'blue', 8)
    cmd3 = DrawCommand(drawable, 50, 60, 'green', 4)
    
    print("\n2. Executing individual commands...")
    cmd1.execute()
    cmd2.execute()
    cmd3.execute()
    
    print(f"Points drawn: {drawable.get_points()}")
    
    print("\n3. Creating and executing macro command...")
    macro = MacroCommand()
    macro.append(DrawCommand(drawable, 70, 80, 'purple', 10))
    macro.append(DrawCommand(drawable, 90, 100, 'orange', 5))
    
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

def guit_demo():
    print(f"\n{'='*60}")
    print("Starting PyQt6 GUI Demo...")
    print("Instructions:")
    print("- Click and drag on the canvas to draw")
    print("- Each drawing operation creates a command")
    print("- Use 'Undo Last' to remove the most recent command")
    print("- Use 'Repaint' to clear and replay all commands")
    print("- Use 'Clear All' to remove all commands")
    print("- Change colors to see different drawing effects")
    print(f"{'='*60}")
    
    app = QApplication(sys.argv)
    
    try:
        window = DrawingApp()
        window.show()
        
        # Run the application
        sys.exit(app.exec())
        
    except KeyboardInterrupt:
        print("\nDemo interrupted by user")
    except Exception as e:
        print(f"Error running GUI demo: {e}")
        import traceback
        traceback.print_exc()

def main():
    print("=== Command Pattern Demo (PyQt6) ===\n")
    
    print("The Command pattern encapsulates requests as objects,")
    print("allowing you to parameterize clients with different requests,")
    print("queue operations, and support undo functionality.\n")
    
    demonstrate_command_pattern()
    # gut_demo()


if __name__ == "__main__":
    main()
