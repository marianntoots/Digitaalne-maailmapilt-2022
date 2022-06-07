from turtle import *

speed(10)

# tausta värv
bgcolor("light blue")

# maja karp
penup()
goto(-100, -100)
pendown()
pensize(3)
color("blue")
begin_fill()
for i in range(4):
    forward(170)
    left(90)
end_fill()

# katus
penup()
goto(-127, 70)
pendown()
color("black")
begin_fill()
for i in range(3):
    forward(225)
    left(120)
end_fill()

# korsten
penup()
goto(20, 130)
pendown()
color("brown", "firebrick")
begin_fill()
for i in range(2):
    forward(40)
    left(90)
    forward(100)
    left(90)
end_fill()

# 1. aken
penup()
goto(0, 0)
pendown()
color("black", "white")
begin_fill()
for i in range(4):
    forward(50)
    left(90)
end_fill()
# akna raam
penup()
goto(25, 0)
pendown()
left(90)
forward(50)

# 2. aken
penup()
goto(-80, 0)
pendown()
right(90)
color("black", "white")
begin_fill()
for i in range(4):
    forward(50)
    left(90)
end_fill()
# akna raam  
penup()
goto(-80, 25)
pendown()
color("black")
forward(50)

# maja uks
penup()
goto(-40, -97)
pendown()
color("red")
begin_fill()
for i in range(2):
    forward(50)
    left(90)
    forward(80)
    left(90)
end_fill()

hideturtle()

