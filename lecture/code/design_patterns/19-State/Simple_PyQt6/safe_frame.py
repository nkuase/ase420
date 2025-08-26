import sys
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QTextEdit, QPushButton, QApplication)
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont
from context import Context
from day_state import DayState

class SafeFrame(QMainWindow, Context):
    """Main GUI window implementing the Context interface for the State pattern.
    
    Note: We inherit from both QMainWindow (PyQt6) and Context (our interface).
    We use regular class inheritance instead of ABC to avoid metaclass conflicts
    between PyQt6's metaclass and ABC's ABCMeta.
    
    This class demonstrates how the State pattern allows the same user actions
    to produce different behaviors based on the current state (day/night).
    
    Key features:
    - Clock display showing current time
    - Log area showing system messages
    - Buttons for safe usage, emergency alarm, and normal calls
    - Automatic state transitions based on time
    """
    
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.setStyleSheet("background-color: lightgray;")
        
        # Initialize with day state
        self.state = DayState.get_instance()
        
        # Current hour for simulation
        self.current_hour = 0
        
        self._create_widgets()
        self._setup_layout()
        self._setup_timer()
        self._center_window()
    
    def _create_widgets(self):
        """Create all GUI widgets."""
        # Clock display - readonly text field
        self.text_clock = QLineEdit()
        self.text_clock.setReadOnly(True)
        self.text_clock.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.text_clock.setStyleSheet("background-color: white; padding: 5px;")
        
        # Log screen - multiline text area
        self.text_screen = QTextEdit()
        self.text_screen.setReadOnly(True)
        self.text_screen.setFont(QFont("Courier", 10))
        self.text_screen.setStyleSheet("background-color: white; padding: 5px;")
        
        # Action buttons
        self.button_use = QPushButton("Use Safe")
        self.button_use.setStyleSheet("background-color: lightblue; padding: 8px;")
        self.button_use.setFont(QFont("Arial", 10))
        self.button_use.clicked.connect(self._on_use)
        
        self.button_alarm = QPushButton("Emergency Alarm")
        self.button_alarm.setStyleSheet("background-color: red; color: white; padding: 8px;")
        self.button_alarm.setFont(QFont("Arial", 10))
        self.button_alarm.clicked.connect(self._on_alarm)
        
        self.button_phone = QPushButton("Normal Call")
        self.button_phone.setStyleSheet("background-color: lightgreen; padding: 8px;")
        self.button_phone.setFont(QFont("Arial", 10))
        self.button_phone.clicked.connect(self._on_phone)
        
        self.button_exit = QPushButton("Exit")
        self.button_exit.setStyleSheet("background-color: gray; padding: 8px;")
        self.button_exit.setFont(QFont("Arial", 10))
        self.button_exit.clicked.connect(self.close)
    
    def _setup_layout(self):
        """Set up the layout of widgets."""
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)
        
        # Add clock display
        main_layout.addWidget(self.text_clock)
        
        # Add log screen (expandable)
        main_layout.addWidget(self.text_screen, 1)  # stretch factor 1
        
        # Create button layout
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        button_layout.addWidget(self.button_use)
        button_layout.addWidget(self.button_alarm)
        button_layout.addWidget(self.button_phone)
        button_layout.addWidget(self.button_exit)
        
        main_layout.addLayout(button_layout)
        
        central_widget.setLayout(main_layout)
    
    def _setup_timer(self):
        """Set up timer for time simulation."""
        self.timer = QTimer()
        self.timer.timeout.connect(self._advance_time)
        self.timer.start(2000)  # Update every 2 seconds
        
        # Set initial time
        self.set_clock(self.current_hour)
    
    def _center_window(self):
        """Center the window on the screen."""
        self.resize(600, 500)
        
        # Get screen geometry
        screen = QApplication.primaryScreen().geometry()
        
        # Calculate center position
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        
        self.move(x, y)
    
    def _advance_time(self):
        """Advance time by one hour (called by timer)."""
        self.current_hour = (self.current_hour + 1) % 24
        self.set_clock(self.current_hour)
    
    def _on_use(self):
        """Handle 'Use Safe' button click."""
        print("Use Safe button clicked")
        self.state.do_use(self)
    
    def _on_alarm(self):
        """Handle 'Emergency Alarm' button click."""
        print("Emergency Alarm button clicked")
        self.state.do_alarm(self)
    
    def _on_phone(self):
        """Handle 'Normal Call' button click."""
        print("Normal Call button clicked")
        self.state.do_phone(self)
    
    # Context interface implementation
    
    def set_clock(self, hour):
        """Update the clock display and trigger state transitions."""
        clock_string = f"Current time: {hour:02d}:00"
        print(clock_string)
        
        self.text_clock.setText(clock_string)
        self.state.do_clock(self, hour)
    
    def change_state(self, state):
        """Change the current state and log the transition."""
        print(f"State changed from {self.state} to {state}")
        self.state = state
        self._append_to_screen(f">>> State changed to {state}")
    
    def call_security_center(self, msg):
        """Send a message to the security center (displayed as CALL)."""
        formatted_msg = f"CALL! {msg}"
        self._append_to_screen(formatted_msg)
    
    def record_log(self, msg):
        """Record a message in the system log (displayed as LOG)."""
        formatted_msg = f"LOG: {msg}"
        self._append_to_screen(formatted_msg)
    
    def _append_to_screen(self, msg):
        """Append a message to the log screen."""
        self.text_screen.append(msg)
        
        # Scroll to bottom
        cursor = self.text_screen.textCursor()
        cursor.movePosition(cursor.MoveOperation.End)
        self.text_screen.setTextCursor(cursor)
