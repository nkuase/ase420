from Shape import Shape

def main():
    line = Shape.create(Shape.TYPECODE_LINE, 0, 0, 100, 200)
    rectangle = Shape.create(Shape.TYPECODE_RECTANGLE, 10, 20, 30, 40)
    oval = Shape.create(Shape.TYPECODE_OVAL, 100, 200, 300, 400)
    
    shapes = [line, rectangle, oval]
    
    for shape in shapes:
        shape.draw()

if __name__ == "__main__":
    main()
