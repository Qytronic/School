import time
from turtle import *

x = 0

def triangle(length, thicness, color):
    pensize(thicness)
    pencolor(color)
    for i in range(3):
        forward(length)
        left(120)


triangle_colors = ["red", "green", "blue"]
for i in range(3):
    triangle(x + 100, 5, triangle_colors[i])
    x += 100


time.sleep(5)
