import random
import turtle
turtle.bgcolor("blue")
screen = turtle.Screen()

numofpoints = 3
xmax = (turtle.window_height()/2)
ymax = (turtle.window_width()/2)
ymin = -ymax
xmin = -xmax

def pointposition():
    Xpos = random.randint(xmin,xmax)
    Ypos = random.randint(ymin,ymax)
    return Xpos,Ypos
turtle.speed(0)

points = []
for i in range(numofpoints):
    points.append(pointposition())
print(points)
turtle.hideturtle()
turtle.penup()
for point in points:
    turtle.setpos(point)
    turtle.dot(10,"white")

turtle.done()
