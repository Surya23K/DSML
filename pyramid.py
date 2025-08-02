import turtle

def draw_square(t, size):
    """Draw a square using turtle t of given size."""
    for _ in range(4):
        t.forward(size)
        t.left(90)     

def draw_pyramid(rows, size):
    """Draw a pyramid with given rows and block size."""
    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    start_x = -rows * size / 2
    start_y = -turtle.window_height() / 2 + 50

    for row in range(rows):
        for block in range(row + 1):
            x = start_x + (size + 5) * (block + (rows - row - 1) / 2)
            y = start_y + row * (size + 5)
            t.goto(x, y)
            t.pendown()
            draw_square(t, size)
            t.penup()

    turtle.done()

# Set parameters
rows = 5
block_size = 40
draw_pyramid(rows, block_size)
