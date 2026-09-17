import time
from turtle import *

x = 0

#Defining a Function that draws triangles horizontally and moving it to insure that the triangles are drawn in each other
def triangle(length, thicness, color):
    pensize(thicness)
    pencolor(color)
    for i in range(3):
        forward(length)
        left(120)
    penup()
    backward(50)
    pendown()
    
triangle_colors = ["red", "green", "blue"]
for i in range(3):
    triangle(x + 100, 5, triangle_colors[i])
    x += 100

time.sleep(5)

