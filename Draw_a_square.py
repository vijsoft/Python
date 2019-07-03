import turtle


def draw_square(turtleObject):  
    count = 4
    while (count > 0):
        turtleObject.forward(100)          
        turtleObject.right(90)
        count -= 1

def draw_circle():
    turtleObject = turtle.Turtle()    # make turtleObject draw a square
    turtleObject.shape("turtle")
    turtleObject.color("yellow")
    turtleObject.circle(100)          


def draw_triangle(turtleObject):
    count = 3
    while (count > 0):
        turtleObject.forward(100)          
        turtleObject.left(120)
        count -= 1

def draw_diamond(turtleObject):
    turtleObject.left(60)
    turtleObject.forward(100) 
    turtleObject.left(60)
    turtleObject.forward(100) 
    turtleObject.left(120)
    turtleObject.forward(100)         
    turtleObject.left(60)
    turtleObject.forward(100)
    turtleObject.left(60)


canvas = turtle.Screen()
canvas.title("Draw Shapes")
canvas.setup(720,480)
#canvas.bgcolor("green")  # default bgcolor is white
yami = turtle.Turtle()    # make turtleObject draw a square
yami.shape("turtle")
yami.color("blue")
yami.shapesize(1)
#yami.width(1.5)
yami.speed(20)

for i in range (0,36):
    draw_diamond(yami)
    yami.right(10)
yami.right(90)
yami.forward(200)
canvas.exitonclick()


##turtle.color('red', 'yellow')
##turtle.begin_fill()
##while True:
##    turtle.forward(200)
##    turtle.left(170)
##    if abs(turtle.pos()) < 1:
##        break
##turtle.end_fill()
##turtle.done()
