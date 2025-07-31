from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGridLayout
from PyQt6.QtCore import Qt
import sys

class IntegerDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.value = 0
        
        # Create labels
        self.octal_label = QLabel("0")
        self.decimal_label = QLabel("0")
        self.hexadecimal_label = QLabel("0")
        
        # Create buttons
        self.increment_button = QPushButton("+")
        self.decrement_button = QPushButton("-")
        
        self.init_ui()
        
    def init_ui(self):
        # Set window title
        self.setWindowTitle("IntegerDisplay")
        
        # Create layout
        layout = QGridLayout()
        layout.addWidget(QLabel("Octal:"), 0, 0)
        layout.addWidget(self.octal_label, 0, 1)
        layout.addWidget(QLabel("Decimal:"), 1, 0)
        layout.addWidget(self.decimal_label, 1, 1)
        layout.addWidget(QLabel("Hexadecimal:"), 2, 0)
        layout.addWidget(self.hexadecimal_label, 2, 1)
        layout.addWidget(self.increment_button, 3, 0)
        layout.addWidget(self.decrement_button, 3, 1)
        
        # Connect buttons
        self.increment_button.clicked.connect(self.increment)
        self.decrement_button.clicked.connect(self.decrement)
        
        self.setLayout(layout)
        self.show()
        
    def increment(self):
        self.set_value(self.value + 1)
        
    def decrement(self):
        self.set_value(self.value - 1)
        
    def get_value(self):
        return self.value
        
    def set_value(self, value):
        self.value = value
        # Update labels with different bases
        self.octal_label.setText(oct(self.value)[2:])  # Remove '0o' prefix
        self.decimal_label.setText(str(self.value))
        self.hexadecimal_label.setText(hex(self.value)[2:])  # Remove '0x' prefix
