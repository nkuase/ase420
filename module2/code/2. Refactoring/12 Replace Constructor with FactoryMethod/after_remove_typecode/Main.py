from Shape import Shape

def main():
    line = Shape.create_line(0, 0, 100, 200)
    rectangle = Shape.create_rectangle(10, 20, 30, 40)
    oval = Shape.create_oval(100, 200, 300, 400)
    
    shapes = [line, rectangle, oval]
    
    for shape in shapes:
        shape.draw()

if __name__ == "__main__":
    main()
