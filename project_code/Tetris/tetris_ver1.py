import pygame
import random

# Global constants - it's OK as it's read only
# code smell - why list when tuple (immutable) is OK? Use immutable objects as much as possible
Colors = [
    (0, 0, 0), # We don't use this 
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# code smell - why use mutable list when tuple (immutable) is OK? Use immutable objects as much as possible
Figures = [
    [[1, 5, 9, 13], [4, 5, 6, 7]],
    [[4, 5, 9, 10], [2, 6, 5, 9]],
    [[6, 7, 9, 10], [1, 5, 6, 10]],
    [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
    [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
    [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
    [[1, 2, 5, 6]],
]
size = (400, 500)

# Global variables (code smell - we should remove them by refactoring)
Type = 0
Color = 0
Rotation = 0

State = "start" # or "gameover"
Field = []

# Tetris block Height and Width
Height = 0
Width = 0
# StartX/Y position in the screen
StartX = 100
StartY= 60
# Block size
Tzoom = 20 # code smell - bad name, can you guess Tzoom from its name? 
# Shift left/right or up/down
ShiftX = 0
ShiftY = 0

# code smell - global variable access, refactor to use
# parameters (if you use a function) or class fields (if you use a class)
def make_figure(x, y):
    global ShiftX, ShiftY, Type, Color, Rotation
    ShiftX = x
    ShiftY = y
    Type = random.randint(0, len(Figures) - 1)
    Color = random.randint(1, len(Colors) - 1)
    Rotation = 0

def intersects(image):
    intersection = False
    # code smell - what is 4? Magic number
    for i in range(4):
        for j in range(4):
            if i * 4 + j in image:
                # out of bounds
                # code smell - confusing, why Y is related i and X is related j?
                if i + ShiftY > Height - 1 or \
                   j + ShiftX > Width - 1 or \
                   j + ShiftX < 0 or \
                   Field[i + ShiftY][j + ShiftX] > 0:
                       intersection = True
    return intersection

def break_lines():
    # code smell - why is it hard to read code? why make two sub-functions
    # for i in ...
    #  is_filled = check_row_filled(...)
    #  if is_filled:
    #.   delete_row(...)
    global Field
    for i in range(1, Height):
        zeros = 0
        for j in range(Width):
            if Field[i][j] == 0:
                zeros += 1
        # there is no empty cell
        if zeros == 0:
            for k in range(i, 1, -1):
                for j in range(Width):
                    Field[k][j] = Field[k - 1][j]

def freeze(image):
    # code smell - can you guess what it does? why there is no comments on what it does, how, and why?
    global Field, State
    for i in range(4):
        for j in range(4):
            if i * 4 + j in image:
                Field[i + ShiftY][j + ShiftX] = Color
    break_lines()
    make_figure(3, 0) 
    if intersects(Figures[Type][Rotation]):
        State = "gameover"

def go_space():
    global ShiftY
    while not intersects(Figures[Type][Rotation]):
        ShiftY += 1
    ShiftY -= 1
    freeze(Figures[Type][Rotation])

def go_down():
    global ShiftY
    ShiftY += 1
    if intersects(Figures[Type][Rotation]):
        ShiftY -= 1 
        freeze(Figures[Type][Rotation])

def go_side(dx):
    global ShiftX
    old_x = ShiftX
    ShiftX += dx
    if intersects(Figures[Type][Rotation]):
        ShiftX = old_x

def rotate():
    global Rotation
    def rotate_figure():
        global Rotation
        Rotation = (Rotation + 1) % len(Figures[Type])
        
    old_rotation = Rotation
    rotate_figure()
    if intersects(Figures[Type][Rotation]):
        Rotation = old_rotation
        
def init_board():
    for i in range(Height):
        new_line = [0] * Width # polymorphism using * 
        Field.append(new_line)

def draw_board(screen, x, y, zoom):
    screen.fill(WHITE)

    for i in range(Height):
        for j in range(Width):
            pygame.draw.rect(screen, GRAY, [x + zoom * j, y + zoom * i, zoom, zoom], 1)
            if Field[i][j] > 0:
                pygame.draw.rect(screen, Colors[Field[i][j]],
                                 [x + zoom * j + 1, y + zoom * i + 1, zoom - 2, zoom - 1])

def draw_figure(screen, image, x, y, shift_x, shift_y, zoom):
    for i in range(4):
        for j in range(4):
            p = i * 4 + j
            if p in image:
                pygame.draw.rect(screen, Colors[Color],
                                 [x + zoom * (j + shift_x) + 1,
                                  y + zoom * (i + shift_y) + 1,
                                  zoom - 2, zoom - 2])
            
def initialize(height, width):
    global Height, Width, Field, State
    Height = height
    Width = width
    Field = []
    State = "start"
    # code smell - why another initializion in the initalize() function?
    init_board()

def main():
    # Pygame related init
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    # we need pressing_down, fps, and counter to go_down() the Tetris Figure
    fps = 200
    counter = 0
    pressing_down = False

    initialize(20, 10) # code smell - what is 20 and 10? Can we use keyword argument? 
    make_figure(3,0)
    done = False
    level = 1
    while not done:
        counter += 1
        if counter > 100000:
            counter = 0
            
        # Check if we need to automatically go down
        if counter % (fps // 2 // level) == 0 or pressing_down: 
            if State == "start":
                go_down()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    rotate()
                if event.key == pygame.K_LEFT:
                    go_side(-1)
                if event.key == pygame.K_RIGHT:
                    go_side(1)
                if event.key == pygame.K_SPACE:
                    go_space()
                if event.key == pygame.K_DOWN:
                    pressing_down = True

            if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                pressing_down = False
                
        draw_board(screen = screen, x = StartX, y = StartY, zoom = Tzoom)
        
        # code smell - how many values duplication Figures[Type][Rotation]
        draw_figure(screen = screen, image = Figures[Type][Rotation], x = StartX, y = StartY, shift_x = ShiftX, shift_y = ShiftY, zoom = Tzoom)

        if State == "gameover":
            done = True

        # refresh the screen
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    main()