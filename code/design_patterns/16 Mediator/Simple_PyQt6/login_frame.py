from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, 
                            QLabel, QButtonGroup, QApplication)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from mediator import MediatorInterface
from colleague_radiobutton import ColleagueRadioButton
from colleague_entry import ColleagueEntry
from colleague_button import ColleagueButton


class LoginFrame(QWidget, MediatorInterface):
    """
    Concrete Mediator that coordinates interactions between UI components
    in a login dialog. Demonstrates the Mediator design pattern.
    """
    
    def __init__(self, title="Login Dialog"):
        super().__init__()
        self.setWindowTitle(title)
        self.setFixedSize(300, 200)
        
        # Create and setup all colleague components
        self.create_colleagues()
        self._setup_layout()
        
        # Initialize the interaction state
        self.colleague_changed()
        
        # Center the window on screen
        self._center_window()
    
    def create_colleagues(self):
        """Create all colleague objects and register them with this mediator."""
        # Radio buttons for login type selection
        self.check_guest = ColleagueRadioButton("Guest")
        self.check_login = ColleagueRadioButton("Login")
        
        # Group radio buttons so only one can be selected
        self.login_type_group = QButtonGroup()
        self.login_type_group.addButton(self.check_guest, 0)  # Guest = 0
        self.login_type_group.addButton(self.check_login, 1)  # Login = 1
        
        # Set Guest as default selection
        self.check_guest.setChecked(True)
        
        # Text entry fields
        self.text_user = ColleagueEntry()
        self.text_user.setPlaceholderText("Enter username")
        
        self.text_pass = ColleagueEntry(echo_mode=ColleagueEntry.EchoMode.Password)
        self.text_pass.setPlaceholderText("Enter password")
        
        # Action buttons
        self.button_ok = ColleagueButton("OK")
        self.button_cancel = ColleagueButton("Cancel")
        
        # Register all colleagues with this mediator
        colleagues = [
            self.check_guest, self.check_login,
            self.text_user, self.text_pass,
            self.button_ok, self.button_cancel
        ]
        
        for colleague in colleagues:
            colleague.set_mediator(self)
        
        # Connect button actions
        self.button_ok.clicked.connect(self._on_ok)
        self.button_cancel.clicked.connect(self._on_cancel)
    
    def _setup_layout(self):
        """Setup the UI layout using PyQt6 layout managers."""
        # Main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # Title
        title_label = QLabel("Mediator Pattern Demo")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        main_layout.addWidget(title_label)
        
        # Form layout using grid
        form_layout = QGridLayout()
        
        # Login type selection
        login_type_layout = QHBoxLayout()
        login_type_layout.addWidget(self.check_guest)
        login_type_layout.addWidget(self.check_login)
        login_type_layout.addStretch()
        
        form_layout.addLayout(login_type_layout, 0, 0, 1, 2)
        
        # Username field
        form_layout.addWidget(QLabel("Username:"), 1, 0)
        form_layout.addWidget(self.text_user, 1, 1)
        
        # Password field
        form_layout.addWidget(QLabel("Password:"), 2, 0)
        form_layout.addWidget(self.text_pass, 2, 1)
        
        main_layout.addLayout(form_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.button_ok)
        button_layout.addWidget(self.button_cancel)
        
        main_layout.addLayout(button_layout)
    
    def colleague_changed(self):
        """
        Mediator's core coordination logic. Called whenever a colleague's state changes.
        This method centralizes all the interaction rules between components.
        """
        if self.check_guest.isChecked():
            # Guest mode: disable username/password fields, enable OK button
            self.text_user.set_colleague_enabled(False)
            self.text_pass.set_colleague_enabled(False)
            self.button_ok.set_colleague_enabled(True)
            
            # Clear fields when switching to guest mode
            self.text_user.clear()
            self.text_pass.clear()
        else:
            # Login mode: enable username field and check user/pass state
            self.text_user.set_colleague_enabled(True)
            self._userpass_changed()
    
    def _userpass_changed(self):
        """
        Handle username/password field coordination logic.
        This demonstrates the mediator managing complex interdependencies.
        """
        username = self.text_user.get_text().strip()
        password = self.text_pass.get_text().strip()
        
        if len(username) > 0:
            # Username entered: enable password field
            self.text_pass.set_colleague_enabled(True)
            
            if len(password) > 0:
                # Both username and password entered: enable OK button
                self.button_ok.set_colleague_enabled(True)
            else:
                # Username but no password: disable OK button
                self.button_ok.set_colleague_enabled(False)
        else:
            # No username: disable password field and OK button
            self.text_pass.set_colleague_enabled(False)
            self.button_ok.set_colleague_enabled(False)
    
    def _center_window(self):
        """Center the window on the screen."""
        screen = QApplication.primaryScreen().geometry()
        window = self.geometry()
        self.move(
            (screen.width() - window.width()) // 2,
            (screen.height() - window.height()) // 2
        )
    
    def _on_ok(self):
        """Handle OK button click."""
        if self.check_guest.isChecked():
            print("Guest login selected")
        else:
            username = self.text_user.get_text()
            password = self.text_pass.get_text()
            print(f"User login: {username} / {'*' * len(password)}")
        
        print("Login process would continue here...")
        self.close()
    
    def _on_cancel(self):
        """Handle Cancel button click."""
        print("Login cancelled")
        self.close()
