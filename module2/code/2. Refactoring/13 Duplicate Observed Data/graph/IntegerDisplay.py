from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGridLayout
from PyQt6.QtCore import Qt
import sys
from ValueListener import ValueListener
from Value import Value
from Graph import Graph

class IntegerDisplay(QWidget, ValueListener):
    def __init__(self):
        super().__init__()
        self.value = Value(0)
        
        # Create labels
        self.octal_label = QLabel("0")
        self.decimal_label = QLabel("0")
        self.hexadecimal_label = QLabel("0")
        
        # Create buttons
        self.increment_button = QPushButton("+")
        self.decrement_button = QPushButton("-")
        
        # Create graphs
        self.graph_circle = Graph.create_graph(Graph.CIRCLE, 100, 100)
        self.graph_rectangle = Graph.create_graph(Graph.RECTANGLE, 100, 50)
        
        # Add listeners to value
        self.value.add_value_listener(self)
        self.value.add_value_listener(self.graph_circle)
        self.value.add_value_listener(self.graph_rectangle)
        
        self.init_ui()
        
    def init_ui(self):
        # Set window title
        self.setWindowTitle("IntegerDisplay with Graphs")
        
        # Create main layout
        main_layout = QVBoxLayout()
        
        # Create top panel with labels and buttons
        panel_layout = QGridLayout()
        panel_layout.addWidget(QLabel("Octal:"), 0, 0)
        panel_layout.addWidget(self.octal_label, 0, 1)
        panel_layout.addWidget(QLabel("Decimal:"), 1, 0)
        panel_layout.addWidget(self.decimal_label, 1, 1)
        panel_layout.addWidget(QLabel("Hexadecimal:"), 2, 0)
        panel_layout.addWidget(self.hexadecimal_label, 2, 1)
        panel_layout.addWidget(self.increment_button, 3, 0)
        panel_layout.addWidget(self.decrement_button, 3, 1)
        
        # Create panel widget
        panel_widget = QWidget()
        panel_widget.setLayout(panel_layout)
        
        # Add components to main layout
        main_layout.addWidget(panel_widget)
        main_layout.addWidget(self.graph_circle)
        main_layout.addWidget(self.graph_rectangle)
        
        # Connect buttons
        self.increment_button.clicked.connect(self.increment)
        self.decrement_button.clicked.connect(self.decrement)
        
        self.setLayout(main_layout)
        self.show()
        
    def increment(self):
        self.set_value(self.value.get_value() + 1)
        
    def decrement(self):
        self.set_value(self.value.get_value() - 1)
        
    def get_value(self):
        return self.value.get_value()
        
    def set_value(self, value):
        self.value.set_value(value)
        
    def value_changed(self, event):
        """Called when value changes (Observer pattern)"""
        if event.get_source() == self.value:
            val = self.value.get_value()
            self.octal_label.setText(oct(val)[2:])  # Remove '0o' prefix
            self.decimal_label.setText(str(val))
            self.hexadecimal_label.setText(hex(val)[2:])  # Remove '0x' prefix
