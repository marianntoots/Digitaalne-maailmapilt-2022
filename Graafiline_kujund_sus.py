import turtle

BODY_COLOR =  'red'
GLASS_COLOR = 'light blue'
BACKBAG_COLOR = 'red'

sus = turtle.Turtle()

def body():
    # turtle suurus ja kiirus
    sus.pensize(20)
    sus.speed(15)

    sus.fillcolor(BODY_COLOR)
    sus.begin_fill()

    # parem pool
    sus.right(90)
    sus.forward(50)
    sus.right(180)
    sus.circle(40, -180)
    sus.right(180)
    sus.forward(200)

    # pea kumerus
    sus.right(180)
    sus.circle(100, -180)

    # vasak pool
    sus.backward(20)
    sus.left(15)
    sus.circle(500, -20)
    sus.backward(20)

    sus.circle(40, -180)
    sus.left(7)
    sus.backward(50)

    sus.up()
    sus.left(90)
    sus.forward(10)
    sus.right(90)
    sus.down()

    sus.right(95)
    sus.forward(50)

    sus.end_fill()


def glass():
    sus.up()
    sus.right(87)
    sus.forward(100)
    sus.left(90)
    sus.forward(20)
    sus.right(90)

    sus.down()
    sus.fillcolor(GLASS_COLOR)
    sus.begin_fill()

    sus.right(150)
    sus.circle(90, -55)

    sus.right(180)
    sus.forward(1)
    sus.right(180)
    sus.circle(10, -65)
    sus.right(180)
    sus.forward(110)
    sus.right(180)
    
    sus.circle(50, -190)
    sus.right(170)
    sus.forward(80)

    sus.right(180)
    sus.circle(45, -30)

    sus.end_fill()

def backpack():
    sus.up()
    sus.right(62)
    sus.forward(100)
    sus.right(90)
    sus.forward(75)

    sus.fillcolor(BACKBAG_COLOR)
    sus.begin_fill()

    sus.down()
    sus.forward(30)
    sus.right(255)

    sus.circle(300, -30)
    sus.right(260)
    sus.forward(30)

    sus.end_fill()

body()
glass()
backpack()
