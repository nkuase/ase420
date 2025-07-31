from Shape import Shape
from ShapeLine import ShapeLine
from ShapeRectangle import ShapeRectangle
from ShapeOval import ShapeOval

def main():
    line = ShapeLine.create(0, 0, 100, 200)
    rectangle = ShapeRectangle.create(10, 20, 30, 40)
    oval = ShapeOval.create(100, 200, 300, 400)
    
    shapes = [line, rectangle, oval]
    
    for shape in shapes:
        shape.draw()

if __name__ == "__main__":
    main()
