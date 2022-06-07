from turtle import *
from random import randint

# funktsioon taime joonistamiseks
def drawTree(level,size,angle,ratio):
  if level >= 0:
    forward(size)
    left(angle)
    drawTree(level-1,size/ratio,angle,ratio)
    right(2*angle)

    drawTree(level-1,size/ratio,angle,ratio)
    left(angle)
    forward(-size)
  else:
    return

# taime joonistamine  
speed(5)
penup()
goto(0,-180)
left(90)
pendown()

# Rekursiooni funktsioon
size = randint(100,140)
angle = randint(20,40) 
ratio = randint(14,18)/10
level = randint(4,6)

drawTree(level,size,angle,ratio)
