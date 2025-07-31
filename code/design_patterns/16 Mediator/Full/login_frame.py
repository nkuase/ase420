"""
Mediator Pattern - Concrete Mediator (LoginFrame)
A concrete mediator that coordinates the interaction between login form components.
"""

import tkinter as tk
from mediator import Mediator
from colleague_radiobutton import ColleagueRadiobutton
from colleague_entry import ColleagueEntry
from colleague_button import ColleagueButton


class LoginFrame(tk.Tk, Mediator):
    """
    Concrete mediator that implements a login dialog.
    Coordinates the behavior of radiobuttons, text fields, and buttons
    to create a cohesive user interface with proper state management.
    """
    
    def __init__(self, title: str):
        """
        Initialize the login frame window.
        
        Args:
            title (str): The window title
        """
        super().__init__()
        self.title(title)
        self.configure(bg='lightgray')
        
        # Create colleagues and set up the interface
        self.create_colleagues()
        self._setup_layout()
        
        # Set initial state
        self.colleague_changed()
        
        # Center the window
        self._center_window()
    
    def create_colleagues(self):
        """
        Create all colleague objects and establish their relationships.
        """
        # Radiobutton variable for guest/login selection
        self.login_type = tk.StringVar(value="guest")
        
        # Create colleague components
        self.check_guest = ColleagueRadiobutton(
            self, "Guest", self.login_type, "guest"
        )
        self.check_login = ColleagueRadiobutton(
            self, "Login", self.login_type, "login"
        )
        
        self.text_user = ColleagueEntry(self, width=20)
        self.text_pass = ColleagueEntry(self, width=20, show='*')
        
        self.button_ok = ColleagueButton(self, "OK", command=self._on_ok)
        self.button_cancel = ColleagueButton(self, "Cancel", command=self._on_cancel)
        
        # Set mediator for all colleagues
        colleagues = [
            self.check_guest, self.check_login,
            self.text_user, self.text_pass,
            self.button_ok, self.button_cancel
        ]
        
        for colleague in colleagues:
            colleague.set_mediator(self)
    
    def _setup_layout(self):
        """Set up the GUI layout."""
        # Use grid layout (4 rows, 2 columns)
        row = 0
        
        # Row 0: Radio buttons
        self.check_guest.grid(row=row, column=0, sticky='w', padx=5, pady=5)
        self.check_login.grid(row=row, column=1, sticky='w', padx=5, pady=5)
        row += 1
        
        # Row 1: Username
        tk.Label(self, text="Username:", bg='lightgray').grid(
            row=row, column=0, sticky='w', padx=5, pady=5
        )
        self.text_user.grid(row=row, column=1, padx=5, pady=5)
        row += 1
        
        # Row 2: Password
        tk.Label(self, text="Password:", bg='lightgray').grid(
            row=row, column=0, sticky='w', padx=5, pady=5
        )
        self.text_pass.grid(row=row, column=1, padx=5, pady=5)
        row += 1
        
        # Row 3: Buttons
        self.button_ok.grid(row=row, column=0, padx=5, pady=5)
        self.button_cancel.grid(row=row, column=1, padx=5, pady=5)
    
    def colleague_changed(self):
        """
        Called when any colleague's state changes.
        Implements the coordination logic between components.
        """
        if self.login_type.get() == "guest":
            # Guest login mode
            self.text_user.set_colleague_enabled(False)
            self.text_pass.set_colleague_enabled(False)
            self.button_ok.set_colleague_enabled(True)
        else:
            # User login mode
            self.text_user.set_colleague_enabled(True)
            self._userpass_changed()
    
    def _userpass_changed(self):
        """
        Handle changes in username/password fields.
        Determines the enabled state of password field and OK button.
        """
        username = self.text_user.get_text()
        password = self.text_pass.get_text()
        
        if len(username) > 0:
            self.text_pass.set_colleague_enabled(True)
            if len(password) > 0:
                self.button_ok.set_colleague_enabled(True)
            else:
                self.button_ok.set_colleague_enabled(False)
        else:
            self.text_pass.set_colleague_enabled(False)
            self.button_ok.set_colleague_enabled(False)
    
    def _center_window(self):
        """Center the window on the screen."""
        self.update_idletasks()
        width = self.winfo_reqwidth()
        height = self.winfo_reqheight()
        pos_x = (self.winfo_screenwidth() // 2) - (width // 2)
        pos_y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
    
    def _on_ok(self):
        """Handle OK button click."""
        login_type = self.login_type.get()
        if login_type == "guest":
            print("Guest login selected")
        else:
            username = self.text_user.get_text()
            password = self.text_pass.get_text()
            print(f"User login: {username} / {'*' * len(password)}")
        
        print("Login process would continue here...")
        self.destroy()
    
    def _on_cancel(self):
        """Handle Cancel button click."""
        print("Login cancelled")
        self.destroy()
