from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt
from ValueListener import ValueListener

class Graph(QWidget, ValueListener):
    """Base graph widget that visualizes values"""
    
    RECTANGLE = 0
    CIRCLE = 1
    
    def __init__(self):
        super().__init__()
        self.graph_value = 0
        
    @staticmethod
    def create_graph(graph_type, width, height):
        """Factory method to create different graph types"""
        if graph_type == Graph.RECTANGLE:
            graph = RectangleGraph()
        elif graph_type == Graph.CIRCLE:
            graph = CircleGraph()
        else:
            raise RuntimeError("Unknown Graph type")
        
        graph.setFixedSize(width, height)
        return graph
        
    def value_changed(self, event):
        """Update graph value and trigger repaint"""
        self.graph_value = event.get_source().get_value()
        self.update()


class RectangleGraph(Graph):
    """Rectangle-based graph visualization"""
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Choose color based on value
        color = QColor("blue") if self.graph_value > 0 else QColor("red")
        painter.setBrush(color)
        
        # Calculate rectangle dimensions
        bounds = self.rect()
        if self.graph_value > 0:
            w = int(bounds.width() / 2 * self.graph_value / 100.0)
            h = bounds.height() // 2
            x = bounds.width() // 2
            y = bounds.height() // 4
        else:
            w = int(bounds.width() / 2 * (-self.graph_value) / 100.0)
            h = bounds.height() // 2
            x = bounds.width() // 2 - w
            y = bounds.height() // 4
            
        painter.fillRect(x, y, w, h, color)


class CircleGraph(Graph):
    """Circle-based graph visualization"""
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Choose color based on value
        color = QColor("blue") if self.graph_value > 0 else QColor("red")
        painter.setBrush(color)
        
        # Calculate arc dimensions
        bounds = self.rect()
        start_angle = 90 * 16  # Qt uses 1/16th degree units
        span_angle = -int(self.graph_value * 10.0 * 16)  # Convert to 1/16th degrees
        
        painter.drawPie(bounds, start_angle, span_angle)
