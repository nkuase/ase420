"""
State Pattern - Concrete Context (SafeFrame)
This class implements the context using a GUI interface.
It demonstrates how the state pattern works with user interactions.
"""

import tkinter as tk
from tkinter import scrolledtext
from context import Context
from state import State
from day_state import DayState


class SafeFrame(tk.Tk, Context):
    """
    Concrete context implementation using tkinter GUI.
    Represents a security system interface that changes behavior based on time of day.
    """
    
    def __init__(self, title: str):
        """
        Initialize the safe frame window.
        
        Args:
            title (str): The window title
        """
        super().__init__()
        self.title(title)
        self.configure(bg='lightgray')
        
        # Initialize with day state
        self.state: State = DayState.get_instance()
        
        # Create GUI components
        self._create_widgets()
        self._setup_layout()
        
        # Center the window
        self._center_window()
    
    def _create_widgets(self):
        """Create all GUI widgets."""
        # Clock display
        self.text_clock = tk.Entry(self, width=60, state='readonly', 
                                  font=('Arial', 12, 'bold'))
        
        # Security center output
        self.text_screen = scrolledtext.ScrolledText(self, width=60, height=15,
                                                   state='disabled', font=('Courier', 10))
        
        # Buttons
        self.button_use = tk.Button(self, text="Use Safe", command=self._on_use,
                                   bg='lightblue', font=('Arial', 10))
        self.button_alarm = tk.Button(self, text="Emergency Alarm", command=self._on_alarm,
                                     bg='red', fg='white', font=('Arial', 10))
        self.button_phone = tk.Button(self, text="Normal Call", command=self._on_phone,
                                     bg='lightgreen', font=('Arial', 10))
        self.button_exit = tk.Button(self, text="Exit", command=self._on_exit,
                                    bg='gray', font=('Arial', 10))
    
    def _setup_layout(self):
        """Set up the GUI layout."""
        # Pack widgets
        self.text_clock.pack(pady=5)
        self.text_screen.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)
        
        # Button frame
        button_frame = tk.Frame(self, bg='lightgray')
        button_frame.pack(pady=5)
        
        self.button_use.pack(in_=button_frame, side=tk.LEFT, padx=5)
        self.button_alarm.pack(in_=button_frame, side=tk.LEFT, padx=5)
        self.button_phone.pack(in_=button_frame, side=tk.LEFT, padx=5)
        self.button_exit.pack(in_=button_frame, side=tk.LEFT, padx=5)
    
    def _center_window(self):
        """Center the window on the screen."""
        self.update_idletasks()
        width = 500
        height = 400
        pos_x = (self.winfo_screenwidth() // 2) - (width // 2)
        pos_y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
    
    # Button event handlers
    def _on_use(self):
        """Handle safe use button click."""
        print("Use Safe button clicked")
        self.state.do_use(self)
    
    def _on_alarm(self):
        """Handle alarm button click."""
        print("Emergency Alarm button clicked")
        self.state.do_alarm(self)
    
    def _on_phone(self):
        """Handle phone button click."""
        print("Normal Call button clicked")
        self.state.do_phone(self)
    
    def _on_exit(self):
        """Handle exit button click."""
        print("Exit button clicked")
        self.destroy()
    
    # Context interface implementation
    def set_clock(self, hour: int):
        """
        Set the current time and update display.
        
        Args:
            hour (int): The current hour (0-23)
        """
        clock_string = f"Current time: {hour:02d}:00"
        print(clock_string)
        
        self.text_clock.config(state='normal')
        self.text_clock.delete(0, tk.END)
        self.text_clock.insert(0, clock_string)
        self.text_clock.config(state='readonly')
        
        self.state.do_clock(self, hour)
    
    def change_state(self, state: State):
        """
        Change to a new state.
        
        Args:
            state (State): The new state to transition to
        """
        print(f"State changed from {self.state} to {state}")
        self.state = state
        
        # Update GUI to reflect state change
        self._append_to_screen(f">>> State changed to {state}")
    
    def call_security_center(self, msg: str):
        """
        Call the security center with a message.
        
        Args:
            msg (str): The message to send to security
        """
        formatted_msg = f"CALL! {msg}"
        self._append_to_screen(formatted_msg)
    
    def record_log(self, msg: str):
        """
        Record a log message.
        
        Args:
            msg (str): The message to log
        """
        formatted_msg = f"LOG: {msg}"
        self._append_to_screen(formatted_msg)
    
    def _append_to_screen(self, msg: str):
        """
        Append a message to the screen output.
        
        Args:
            msg (str): The message to append
        """
        self.text_screen.config(state='normal')
        self.text_screen.insert(tk.END, msg + '\n')
        self.text_screen.see(tk.END)
        self.text_screen.config(state='disabled')
