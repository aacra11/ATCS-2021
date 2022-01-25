import turtle

def spiral(initialLength, angle, multiplier):
    if (initialLength < 1) or (initialLength > 200):
        turtle.right(angle)
        turtle.forward(initialLength*multiplier)
        return
    turtle.forward(initialLength)
    turtle.right(angle)
    spiral(initialLength*multiplier, angle, multiplier)

def tree(initialLength, height):
    if height > 0:
        turtle.forward(initialLength)
        turtle.right(30)
        tree(initialLength/2, height-1)
        turtle.left(60)
        tree(initialLength/2, height-1)
        turtle.right(30)
        turtle.backward(initialLength)

def snowflakeSide(sideLength, levels):
    if levels == 0:
        turtle.forward(sideLength)
        return
    sideLength = sideLength/3
    snowflakeSide(sideLength, levels-1)
    turtle.left(60)
    snowflakeSide(sideLength, levels-1)
    turtle.right(120)
    snowflakeSide(sideLength, levels-1)
    turtle.left(60)
    snowflakeSide(sideLength, levels-1)

def snowflake(sideLength, levels):
    turtle.left(60)
    snowflakeSide(sideLength, levels)
    turtle.right(120)
    snowflakeSide(sideLength, levels)
    turtle.right(120)
    snowflakeSide(sideLength, levels)
    turtle.right(120)
